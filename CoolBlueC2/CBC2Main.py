#   #   #   #   #   #   #   #   #   #   #   #   #   #   #

#       This is the main controller of the menu         #
#             built from looking at empire              #

#   #   #   #   #   #   #   #   #   #   #   #   #   #   #
import cmd


class MainMenu(cmd.Cmd):
    # this is where it all starts and is the menu driver

    def __init__(self):
        cmd.Cmd.__init__(self)

        self.run = True
        self.menu_state = "Main"
        self.prompt = "[CoolBlue] > "
        self.resourceQueue = []

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
                        self.do_exit("")
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
            agents_menu = AgentsMenu(self)
            agents_menu.cmdloop()
        except Exception:
            pass

    def do_listeners(self, line):
        """"Enter the Listeners Menu"""
        try:
            print("Moving to listeners Menu")
            listeners_menu = ListenersMenu(self)
            listeners_menu.cmdloop()
        except Exception:
            pass

    def do_payloads(self, line):
        """"Enter the Payloads Menu"""
        try:
            print("Moving to Payloads Menu")
            payloads_menu = PayloadsMenu(self)
            payloads_menu.cmdloop()
        except Exception:
            pass


class SubMenu(cmd.Cmd):

    def __init__(self, mainMenu):
        cmd.Cmd.__init__(self)
        self.mainMenu = mainMenu

    def cmdloop(self):
        cmd.Cmd.cmdloop(self)

    def emptyline(self):
        pass

    def postcmd(self, stop, line):
        if line == "back":
            return True
        if len(self.mainMenu.resourceQueue) > 0:
            nextcmd = self.mainMenu.resourceQueue.pop(0)
            if nextcmd == "lastautoruncmd":
                raise Exception("endautorun")
            self.cmdqueue.append(nextcmd)

    def do_back(self, line):
        """Go back a menu."""
        return True

    def do_listeners(self, line):
        """Jump to the listeners menu."""
        raise NavListeners()

    def do_agents(self, line):
        """Jump to the agents menu."""
        raise NavAgents()

    def do_main(self, line):
        """Go back to the main menu."""
        raise NavMain()

    def do_exit(self, line):
        """Exit CoolBLue."""
        raise KeyboardInterrupt

    def do_creds(self, line):
        """Display/return credentials from the database."""
        self.mainMenu.do_creds(line)

    # print a nicely formatted help menu
    #   stolen/adapted from recon-ng which yet again stolen from empire
    def print_topics(self, header, commands, cmdlen, maxcol):
        if commands:
            self.stdout.write("%s\n" % str(header))
            if self.ruler:
                self.stdout.write("%s\n" % str(self.ruler * len(header)))
            for command in commands:
                self.stdout.write("%s %s\n" % (command.ljust(17), getattr(self, 'do_' + command).__doc__))
            self.stdout.write("\n")


# custom exceptions used for nested menu navigation
class NavMain(Exception):
    """
    Custom exception class used to navigate to the 'main' menu.
    """

    pass


class NavAgents(Exception):
    """
    Custom exception class used to navigate to the 'agents' menu.
    """
    pass


class NavListeners(Exception):
    """
    Custom exception class used to navigate to the 'listeners' menu.
    """
    pass


class AgentsMenu(SubMenu):
    def __init__(self, MainMenu):
        SubMenu.__init__(self, MainMenu)

        self.doc_header = "Commands"

        self.prompt = "[CooLBLue-Agents] > "

        def do_back(self, line):
            """
            Go Back to Main Menu
            """


class PayloadsMenu(SubMenu):
    def __init__(self, MainMenu):
        SubMenu.__init__(self, MainMenu)

        self.doc_header = "Commands"

        self.prompt = "[CooLBLue-Payloads] > "

        def do_back(self, line):
            """
            Go Back to Main Menu
            """


class ListenersMenu(SubMenu):
    def __init__(self, MainMenu):
        SubMenu.__init__(self, MainMenu)

        self.doc_header = "Commands"

        self.prompt = "[CooLBLue-Listeners] > "

        def do_back(self, line):
            """
            Go Back to Main Menu
            """
