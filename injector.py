import pymem, sys
from colorama import Fore

w = Fore.WHITE
lg = Fore.LIGHTGREEN_EX
bl = Fore.BLACK
rd = Fore.RED
lb = Fore.LIGHTBLUE_EX

def injecting(proc_name, dll_path):
    try:
        mem = pymem.Pymem(proc_name)
        dllpath_bytes = dll_path.encode('utf-8')
        remote_alloc = mem.allocate(len(dllpath_bytes))
        mem.write_bytes(remote_alloc, dllpath_bytes)
        loadlib_addr = mem.get_module('kernel32.dll').lpBaseOfDll + 0xC90
        mem.create_remote_thread(loadlib_addr, remote_alloc)
        print(f"{lg}[{w}*{lg}] {bl}- {w}Succesfully Injected DLL to {proc_name}")
    except Exception as e:
        print(f"{rd}[{w}!{rd}] {bl}- {w}Error: {e}")
        
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"{lb}[{w}+{lb}] {bl}- {w}Usage: python injector.py <proccess name> <dll path for inject>")
        sys.exit(1)
    proc_name = sys.argv[1]
    dll_path = sys.argv[2]
    
    injecting(proc_name, dll_path)