from read_data import read_data

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    names = []
    for msg in data['messages']:
        name = msg.get('actor', False)
        if name:
            if name not in names:
                names.append(name)
        name = msg.get('from', False)
        if name:
            if name not in names:
                names.append(name)
            
    return len(names)
    users_name = ['Jalilov', 'Oybek', 'K Sharof', 'Murodjon TATU', 'Рахимов Мухаммад Бобур', 'K Diyor', 'Hamid aka', 'Codeschooluz', '(; Sulaymon ;)', 'Odilxon', '✪ Black Coder ✪', 'Rasulov Diyorbek', 'Shohjahon Berdimurotov', 'Malik Domla', 'Shahzod', 'Ochilov Elbek', 'ᴏᴛᴀʏᴏʀ ʏᴜsᴜᴘᴏᴠ', 'Jamshid', 'O`razg`ali', 'K Ikrom', 'Feruz Bekkiyev', '👨\u200d🎓 Ｓ@რץβογ 👨\u200d💻', 'ابراهيم', 'Muhammad Ali 🇺🇿', 'Mukhriddin', 'Husan', 'SARVARBEK JAKBAROV DI-11-21', 'Olimoff', 'Python 2022A : CHAT', 'Zarif Aka Ustoz', 'Diyorbek', 'K Otabek', 'رَوْشاَن', '꧁❀ιѕяσιℓ❀꧂', 'Bilol', 'Python 2022 A', 'Doniyor Baltashov', 'Jasurbek K Husan', 'Elmurod Shoyimov', 'Ziyodulloh Abduvali', 'Mahliyoxon Anvarova']
    return len(users_name)



data = read_data('data/result.json')
print(find_all_users_name(data))
