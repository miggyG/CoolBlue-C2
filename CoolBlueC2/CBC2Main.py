#   #   #   #   #   #   #   #   #   #   #   #   #   #   #

#       This is the main controller of the menu         #
#             built from looking at empire              #

#   #   #   #   #   #   #   #   #   #   #   #   #   #   #
import cmd
import readline
import sys


class MainMenu(cmd.Cmd):
    # this is where it all starts and is the menu driver

    def __init__(self):
        cmd.Cmd.__init__(self)

        self.run = True
        self.menu_state = "Main"
        self.prompt = "[CoolBlue] > "

    def cmdloop(self):
        while self.run:
            try:
                if self.menu_state == "Agents":
                    self.agentsmenu("")
                elif self.menu_state == "Listeners":
                    self.listenersmenu("")
                else:
                    # we in main menu
                    cmd.Cmd.cmdloop(self)

            except KeyboardInterrupt:
                # pulled directly from empire
                self.menu_state = "Main"
                try:
                    confirmexit = input("\nExit? [y/N] ")
                    if confirmexit.lower() != "" and confirmexit.lower()[0] == "y":
                        self.do_exit()
                    else:
                        continue
                except KeyboardInterrupt:
                    continue

    def do_exit(self, line):
        """Exit CoolBlue-C2"""
        # put any shut down actions here
        print("Shutting Down...")
        self.run = False

    def do_agents(self, line):
        """Enter the Agents Menu"""
        try:
            print("Moving to Agents Menu")
        except Exception as e:
            raise e

    def do_listeners(self, line):
        """"Enter the Listeners Menu"""
        try:
            print("Moving to listeners Menu")
        except Exception as e:
            raise e

    def do_payloads(self, line):
        """"Enter the Payloads Menu"""
        try:
            print("Moving to Payloads Menu")
        except Exception as e:
            raise e
