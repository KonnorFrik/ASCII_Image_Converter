|===-Convert image to ascii art-===|
|                                  |
|==========-Description-===========|
| Script read image, convert it to |
| Black & White, replace each      |
| pixel with symbol and print to   |
| standard output or given file.   |
|==================================|
|                                  |
|=====-Command Line Arguments-=====|
| '-b' or '--block_size' size      |
|     Each sector 'n x n'          |
|     where 'n' is 'block_size'    |
|     will be compressed to one    |
|     pixel.                       |
|==================================|
| '-r' or '--reverse'              |
|     Make reversed image.         |
|     Dark pixel become to light   |
|     and vise versa.              |
|==================================|
| '-h' or '--help'                 |
|     Show help message            |
|==================================|
| '-o' or '--output' filename      | 
|     Write result symbolic image  |
|     to file with 'filename'      |
|==================================|
| filename                         |
|     Required positional argument |
|     Convert image with           |
|     'filename'                   |
|==================================|
