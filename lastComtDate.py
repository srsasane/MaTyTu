import subprocess

def get_last_commit_date():
    try:
        output = subprocess.check_output(['git', 'log', '-1', '--format=%cd'])
        return output.decode('utf-8').strip()
    except Exception as e:
        return "Unknown"

# last_commit_date = get_last_commit_date()
# print("Last commit date:", last_commit_date)
