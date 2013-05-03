"""
McCabe plugin for PyLint.
"""

import ast

from mccabe import McCabeChecker

from pylint.interfaces import IRawChecker
from pylint.checkers import BaseChecker


class McCabe(BaseChecker):
    """
    Check a module's McCabe complexity rating.
    """

    __implements__ = IRawChecker

    name = 'mccabe'
    msgs = {
        'C0901': ('%s', 'Code is too complex'),
    }
    options = (
        ('max-complexity', {'group': 'design',
                            'default': 10,
                            'type': 'int',
                            'metavar': '<int>',
                            'help': 'Maximum complexity allowed.',
                            }),
    )

    def set_option(self, optname, value, action=None, optdict=None):
        super(McCabe, self).set_option(optname, value, action, optdict)

    def process_module(self, node):
        """
        Check complexity for a module.
        """
        code = node.file_stream.read()

        try:
            tree = compile(code, node.file, "exec", ast.PyCF_ONLY_AST)
        except SyntaxError:
            # Pylint would have already failed
            return

        McCabeChecker.max_complexity = self.config.max_complexity
        results = McCabeChecker(tree, node.file).run()
        for lineno, _, text, _ in results:
            text = text[5:]
            self.add_message('C0901', line=lineno, args=text)


def register(linter):
    """
    Register McCabe checker with PyLint.
    """
    linter.register_checker(McCabe(linter))
