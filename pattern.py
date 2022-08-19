import rich
from rich.console import Console 
console = Console()

U = ['*       *',
     '*       *',
     '*       *',
     '*       *',
     '  * * *  ']
N = ['*       *',
     '* *     *',
     '*   *   *',
     '*     * *',
     '*       *']
I = [
    '**********',
    '    *     ',
    '    *     ',
    '    *     ',
    '**********',]
X = ['*        *  ',
     '  *    *    ',
     '    *      ',
     '  *    *    ',
     '*        *  ']
line0 = '             '.join(i[0] for i in (U,N,I,X))
line1 = '             '.join(i[1] for i in (U,N,I,X))
line2 = '             '.join(i[2] for i in (U,N,I,X))
line3 = '             '.join(i[3] for i in (U,N,I,X))
line4 = '             '.join(i[4] for i in (U,N,I,X))

def _prnt():
    for l in (line0, line1, line2, line3, line4):
        console.print(l, style="bold chartreuse1")