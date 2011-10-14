# -*- mode: python; coding: utf-8 -*-
#
# Copyright 2011 Andrej A Antonov <polymorphm@qmail.com>.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

assert str is not bytes

from . import fix_cyrillic_coding

def main():
    from argparse import ArgumentParser
    
    parser = ArgumentParser(
            description='Utility for massive fixing of `txt`-files encoding')
    parser.add_argument('path', nargs='+',
            help='path to txt-file of directory of txt-files')
    parser.add_argument('--quiet', action='store_true',
            help='quiet (no output)')
    parser.add_argument('--followlinks', action='store_true',
            help='follow symbolic links. '
                    'it can lead to infinite recursion '
                    'if a link points to a parent directory of itself')
    parser.add_argument('--extension',
            help='non-standard of txt-file extension')
    args = parser.parse_args()
    
    if not args.quiet:
        from .safe_print import safe_print as log
    else:
        log = None
    
    fix_cyrillic_coding(
            args.path,
            log=log,
            followlinks=args.followlinks,
            extension=args.extension)
