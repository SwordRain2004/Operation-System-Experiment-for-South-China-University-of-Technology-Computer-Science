import os
import sys
history = []


def execute_command(command):
    global history
    if command.strip():
        history.append(command)
        if len(history) > 10:
            history.pop(0)
    args = command.split()
    if not args:
        return
    if args[0] == "exit":
        print("Exiting the shell.")
        sys.exit(0)
    elif args[0] == "cd":
        try:
            os.chdir(args[1])
        except IndexError:
            print("cd: missing argument")
        except FileNotFoundError:
            print(f"cd: no such file or directory: {args[1]}")
        return
    elif args[0] == "history":
        for i, cmd in enumerate(history, start=1):
            print(f"{i}: {cmd}")
        return
    try:
        pid = os.fork()
        if pid == 0:
            try:
                os.execvp(args[0], args)
            except FileNotFoundError:
                print(f"{args[0]}: command not found")
            sys.exit(1)
        else:
            os.wait()
    except OSError as e:
        print(f"Fork failed: {e}")


def main():
    print("Simple Command Interpreter, type:"
          "\n'cd directory_to_open' to switch to the specified directory)"
          "\n'history' to display the last 10 executed historical commands"
          "\n'exit' to quit")
    while True:
        try:
            command = input(f"{os.getcwd()} >>> ")
            execute_command(command)
        except EOFError:
            print("\nExiting the shell.")
            break
        except KeyboardInterrupt:
            print("\nUse 'exit' to quit the shell.")


if __name__ == "__main__":
    main()
