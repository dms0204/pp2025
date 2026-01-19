import subprocess
import shlex

def run_command(cmd):
    # Pipe
    if "|" in cmd:
        parts = [shlex.split(p.strip()) for p in cmd.split("|")]
        p1 = subprocess.Popen(parts[0], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(parts[1], stdin=p1.stdout)
        p1.stdout.close()
        p2.communicate()
        return

    # Redirect output >
    if ">" in cmd:
        command, outfile = cmd.split(">")
        with open(outfile.strip(), "w") as f:
            subprocess.run(shlex.split(command), stdout=f)
        return

    # Redirect input <
    if "<" in cmd:
        command, infile = cmd.split("<")
        with open(infile.strip(), "r") as f:
            subprocess.run(shlex.split(command), stdin=f)
        return

    # Normal command
    subprocess.run(shlex.split(cmd))


def main():
    while True:
        try:
            cmd = input("myshell> ")
            if cmd in ["exit", "quit"]:
                break
            run_command(cmd)
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()