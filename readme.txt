|===-Convert image to ascii art-===|       B B B B B B B B B B B B B B B B B B B B B B B B B B B B    
|                                  |     B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B  
|==========-Description-===========|   B B B B B B B B B B B                     B B B B B B B B B B B
| Script read image, convert it to |   B B B B B B B B B B   B B B B B B B B B B   B B B B B B B B B B
| Black & White, replace each      |   B B B B B B B B B   B B B B B B B B B B B B   B B B B B B B B B
| pixel with symbol and print to   |   B B B B B B B B   B B B B B B B B B B B B B B   B B B B B B B B
| standard output or given file.   |   B B B B B B B   B B B B B B B B B B B B B B B B   B B B B B B B
|==================================|   B B B B B B   B B B B B B B B B B B B B B B B B B   B B B B B B
|                                  |   B B B B B   B B B B B B B B B B B B B B B B B B B B   B B B B B
|=====-Command Line Arguments-=====|   B B B B   B B B B B B B B B B B B B B B B B B B B B B   B B B B
| '-b' or '--block_size' size      |   B B B   B B B B B B B   B B B B B B B B   B B B B B B B   B B B
|     Each sector 'n x n'          |   B B   B B B B B B B   B   B B B B B B   B   B B B B B B B   B B
|     where 'n' is 'block_size'    |   B B   B B B B B B   B   B   B B B B   B B B   B B B B B B   B B
|     will be compressed to one    |   B B   B B B B B B   B B B   B B B B B B B B B B B B B B B   B B
|     pixel.                       |   B B   B B B B B B B       B B B B B B B B B B B B B B B B   B B
|==================================|   B B   B B B B B B B B B B B B B B B B B B B B B B B B B B   B B
| '-r' or '--reverse'              |   B B   B B B B B B B B B B B B B B B B B B B B B B B B B B   B B
|     Make reversed image.         |   B B   B B B B B B B B B B B B B B B B B B B B B B B B B B   B B
|     Dark pixel become to light   |   B B   B B B B B B B B B B B B B B B B B B B B B B B B B B   B B
|     and vise versa.              |   B B   B B B B B B B B B B B B B B B B B B B B B B B B B B   B B
|==================================|   B B   B B B B B B B B B B B B B B B B B B B B B B B B B B   B B
| '-h' or '--help'                 |   B B B   B B B B B B     B B B B B B B B     B B B B B B   B B B
|     Show help message            |   B B B B   B B B B B B B   B B B B B B   B B B B B B B   B B B B
|==================================|   B B B B B   B B B B B B B             B B B B B B B   B B B B B
| '-o' or '--output' filename      |   B B B B B B   B B B B B B B B B B B B B B B B B B   B B B B B B
|     Write result symbolic image  |   B B B B B B B   B B B B B B B B B B B B B B B B   B B B B B B B
|     to file with 'filename'      |   B B B B B B B B   B B B B B B B B B B B B B B   B B B B B B B B
|==================================|   B B B B B B B B B   B B B B B B B B B B B B   B B B B B B B B B
| filename                         |   B B B B B B B B B B   B B B B B B B B B B   B B B B B B B B B B
|     Required positional argument |   B B B B B B B B B B B                     B B B B B B B B B B B
|     Convert image with           |     B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B  
|     'filename'                   |       B B B B B B B B B B B B B B B B B B B B B B B B B B B B    
|==================================|   
