def buildGrid(dest):
  f = open(dest, 'r')
  f_str = f.read()
  return [list(x) for x in f_str.split('\n')][0:-1]
