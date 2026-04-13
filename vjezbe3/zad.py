import Projectile as p

s=p.Projectile(15, 45, 1, 1, 1)
s.graf()
print('za dt<=0.2 se prepoznaje o čemu je riječ iako je dosta neprecizno. Tek za dt<=0.001 dobijamo zadovoljavajuće rješenje.')
