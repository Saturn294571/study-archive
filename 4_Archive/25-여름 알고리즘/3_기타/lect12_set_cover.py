#Set Covering
states_needed = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

stations = {} 
stations[1] = set([1,2,3,8])
stations[2] = set([1,2,3,4,8])
stations[3] = set([1,2,3,4])
stations[4] = set([2,3,4,5,7,8])
stations[5] = set([4,5,6,7])
stations[6] = set([5,6,7,9,10])
stations[7] = set([4,5,6,7])
stations[8] = set([1,2,4,8])
stations[9] = set([6,9])
stations[10] = set([6,10])
 
final_stations = set()
 
while states_needed:
  best_station = None
  states_covered = set()
 
  for station, states in stations.items():
    covered = states_needed & states

    if len(covered) > len(states_covered):
      best_station = station
      states_covered = covered
 
  states_needed -= states_covered
  final_stations.add(best_station)
 
print(final_stations)
