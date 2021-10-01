players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

team_a_rest = [players_dict[players]['name']
               for players in players_dict
               if players_dict[players]['team'] == 'A' and players_dict[players]['status'] == 'Rest']

team_b_Training = [players_dict[players]['name']
                   for players in players_dict
                   if players_dict[players]['team'] == 'B' and players_dict[players]['status'] == 'Training']

team_c_Travel = [players_dict[players]['name']
                 for players in players_dict
                 if players_dict[players]['team'] == 'C' and players_dict[players]['status'] == 'Travel']

print('team_a_rest: ', team_a_rest)
print('team_B_Training: ', team_b_Training)
print('team_c_rest:', team_c_Travel)
