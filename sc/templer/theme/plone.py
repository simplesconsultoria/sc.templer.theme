# -*- coding:utf-8 -*-
import copy

from templer.core.base import get_var
from templer.core.vars import EXPERT

from sc.templer.core.base import PlonePackage


class PloneTheme(PlonePackage):

    summary = "A theme package following the Simples Consultoria standards"
    help = "A package that will configure a Plone theme installation"

    category = "Simples Consultoria - Themes"

    _template_dir = "templates/plonetheme"
    vars = copy.deepcopy(PlonePackage.vars)

    get_var(vars, 'plone_version').modes = (EXPERT, )
    get_var(vars, 'keywords').default = 'plone theme simples_consultoria'

    def check_vars(self, vars, cmd):
        responses = super(PloneTheme, self).check_vars(vars, cmd)
        return responses
