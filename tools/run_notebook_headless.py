"""Headless, single-pass execution of a notebook with the kernel of the pinned environment.
Usage: python tools/run_notebook_headless.py <notebook.ipynb> [kernel_name]   (default kernel: python3)
The notebook is executed in its own folder (relative paths of the notebook stay valid), top to bottom, once.
After EVERY cell the notebook file is saved with the outputs so far, so an interrupted run leaves a readable record.
A line per cell is appended to <notebook folder>/../RUN_LOG.txt (the run log; never inside results/).
Exit code 0: all cells ran; 1: a cell raised (the notebook is saved with the traceback in that cell).
Release RENE-D-26-09232-R2: the final run was executed with this script (kernel name 'rene-r2', a kernel registered
for the pinned environment); the only changes since are this docstring, the name of the log file and the default
kernel name 'python3', the kernel that ipykernel installs into the environment of requirements.txt."""
import os, re, sys, time, datetime
import asyncio
if sys.platform == 'win32':                                   # pyzmq needs the selector event loop on Windows
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
try:                                                          # the log line may contain non-ASCII text of a cell
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass
import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

path = os.path.abspath(sys.argv[1]); kernel = sys.argv[2] if len(sys.argv) > 2 else 'python3'
folder = os.path.dirname(path)
logfile = os.path.abspath(os.path.join(folder, '..', 'RUN_LOG.txt'))   # next to notebooks/, never inside results/ (the notebook refuses a non-empty unstamped results folder)
nb = nbformat.read(path, as_version=4)
t0 = {}

def log(msg):
    line = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S} | {msg}"
    print(line, flush=True)
    with open(logfile, 'a', encoding='utf-8') as fh:
        fh.write(line + '\n')

def save():
    tmp = path + '.tmp'
    nbformat.write(nb, tmp)
    os.replace(tmp, path)

async def on_start(cell, cell_index):
    t0[cell_index] = time.time()
    first = (cell.source.strip().splitlines() or [''])[0][:80]
    log(f"cell {cell_index} started | {first}")

async def on_done(cell, cell_index, execute_reply):
    save()
    status = execute_reply['content'].get('status', '?') if execute_reply else '?'
    log(f"cell {cell_index} finished | {status} | {time.time() - t0.get(cell_index, time.time()):.1f} s")

client = NotebookClient(nb, kernel_name=kernel, timeout=None, resources={'metadata': {'path': folder}},
                        on_cell_execute=on_start, on_cell_executed=on_done, record_timing=True)
log(f"run started | notebook {os.path.basename(path)} | kernel {kernel} | code cells {sum(c.cell_type == 'code' for c in nb.cells)}")
try:
    client.execute()
except CellExecutionError as e:
    last = re.sub(r'\x1b\[[0-9;]*m', '', str(e).splitlines()[-1]) if str(e) else type(e).__name__
    save(); log(f"RUN STOPPED: a cell raised | {last[:300]}")
    sys.exit(1)
except BaseException as e:
    save(); log(f"RUN STOPPED: {type(e).__name__}: {str(e)[:300]}")
    raise
save(); log("run finished | all cells executed")
