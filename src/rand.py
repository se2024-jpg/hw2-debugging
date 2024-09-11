import subprocess

def random_array(arr):
    shuffled_num = None
    for i in range(0,len(arr)):
        # Correcting the arguments passed to subprocess.run
        shuffled_num = subprocess.run(["shuf", "-i", "1-20", "-n", "1"], capture_output=True, text=True)
        
        # Fixing int() conversion by specifying base as 10 and using decoded output
        arr[i] = int(shuffled_num.stdout.strip(), base=10)  
    return arr
