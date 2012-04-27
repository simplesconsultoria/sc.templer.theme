# -*- coding:utf-8 -*-
import copy

from templer.core.base import get_var
from templer.core.vars import EXPERT

from sc.templer.core.base import PlonePackage

class Diazo(PlonePackage):

    summary = "Create a Diazo theme based on beyondskins.responsive."
    help = """This template allows you to create a Diazo theme based on
              beyondskins.responsive"""

    category = "Simples Consultoria - Themes"

    _template_dir = "templates/diazo"

    vars = copy.deepcopy(PlonePackage.vars)

    get_var(vars, 'plone_version').modes = (EXPERT, )
    get_var(vars, 'keywords').default = 'plone theme simples_consultoria'

    def check_vars(self, vars, cmd):
        responses = super(Diazo, self).check_vars(vars, cmd)
        return responses
