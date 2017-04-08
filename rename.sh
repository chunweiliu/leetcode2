dash="_"
hyphen="-"

for file in *
do
  cmd="mv $file ${file//$hyphen/$dash}"
  echo $cmd
  $cmd
done