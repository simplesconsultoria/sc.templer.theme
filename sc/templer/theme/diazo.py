# -*- coding:utf-8 -*-
import copy

from templer.core.base import BaseTemplate

from templer.core.vars import DottedVar
from templer.core.vars import StringVar

from templer.core.vars import EASY
from templer.core.vars import EXPERT

from sc.templer.core import DEFAULTS as D


class Diazo(BaseTemplate):

    summary = "Create a Diazo theme based on beyondskins.responsive."
    help = """This template allows you to create a Diazo theme based on
              beyondskins.responsive"""

    category = "Simples Consultoria"

    ndots = 1
    use_cheetah = True

    required_templates = []
    default_required_structures = []
    _template_dir = "templates/diazo"

    vars = copy.deepcopy(BaseTemplate.vars)
    vars += [
        StringVar(
            'title',
            title='Title',
            description='Theme title',
            default='Beyondskins Theme',
            modes=(EASY, EXPERT),
            page='Metadata',
            help="""A friendly name for this theme."""),

        DottedVar(
            'namespace_package',
            title='Namespace Package Name',
            description='Name of outer namespace package',
            default='beyondskins',
            modes=(EXPERT, ),
            page='Namespaces',
            help="""First level name for the diazo theme."""
        ),

        DottedVar(
            'package',
            title='Package Name',
            description='Name of the inner namespace package',
            default='theme',
            modes=(EXPERT, ),
            page='Namespaces',
            help="""Second level name for the diazo theme."""),

        StringVar(
            'version',
            title='Version',
            description='Version number for project',
            default='1.0',
            modes=(EASY, EXPERT),
            page='Metadata',
            help="""Version number"""
            ),

        StringVar(
            'description',
            title='Description',
            description='One-line description of the project',
            default='Diazo Theme developed by Simples Consultoria',
            modes=(EASY, EXPERT),
            page='Metadata',
            help="""Description of this theme."""
            ),

        StringVar(
            'author',
            title='Author',
            description='Name of author for project',
            default= D.get('author'),
            modes=(),
            page='Metadata',
            help="""Name that will appear on the theme description"""
            ),

        StringVar(
            'author_email',
            title='Author Email',
            description='Email of author for project',
            default = D.get('email'),
            modes=(),
            page='Metadata',
            help="""Email of the author of the theme."""
            ),
    ]

    def check_vars(self, vars, command):
        if not command.options.no_interactive and \
           not hasattr(command, '_deleted_once'):
            del vars['package']
            command._deleted_once = True
        return super(Diazo, self).check_vars(vars, command)
