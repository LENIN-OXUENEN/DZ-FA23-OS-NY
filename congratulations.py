import time
import random
import getpass

user=getpass.getuser()
def generate_text():
    br = '<br>'
    greeting = random.choice(['Дорогой', "Милый", 'Драгоценный мой', 'Уважаемый', 'Любимый', 'Здравствуй', 'Прекрасный друг'])
    year_desc = random.choice(['не простым', 'не из лёгких', 'неоднозначным', 'противоречивым', 'словно испытание', 
                               'полон проблем', 'проблемным', 'не всегда удачным', 'вызовами', 'сложным'])
    conjunction = random.choice(['одновременно', 'вместе с тем', 'также', 'в то же время', 'при этом', 'и в тоже время'])
    year_positive = random.choice(['ярким на события', 'насыщенным', 'радостным', 'полным эмоций', 'запоминающимся', 
                                   'непохожим на другие', 'не лишенным радостей', 'свежим', 'светлым', 'насыщенным'])
    appreciation = random.choice(['И я ценю твой вклад в это', 'И это не без твоей помощи', 'И ты помог(ла) этому осуществиться', 
                                 'И только благодаря твоей поддержке, я справился(лась)', 'Ты стал(а) неотъемлемой частью моего успеха', 
                                 'И твоё участие было очень важным'])

    heartfelt = random.choice(['От всей души', 'От всего сердца', 'Искренне', 'Затая дыхание', 'С надеждой на будущее', 
                               'С любовью в сердце', 'Сердечно', 'С благодарностью', 'С теплотой'])
    wishes = random.choice(['у тебя все будет так, как ты захочешь', 'будет меньше грусти и забот и побольше радости', 
                            'все твои мечты сбудутся', 'подарки сыпятся как из Рога изобилия', 'все планы реализуются', 
                            'тебе всегда сопутствует удача', 'радость наполнит каждый твой день', 'улыбки будут чаще, а грусть останется в прошлом', 
                            'все неприятности останутся в прошлом', 'плохое забудется, а хорошее приумножится', 'будет море позитива'])
    aspirations = random.choice(['тебе всегда сопутствовала удача', 'вдохновение не покидало тебя', 'тебе удалось воплотить всё задуманное', 
                                'о тебе слагали легенды', 'год принёс лишь радости', 'радостные дни сменялись ещё более радостными', 
                                'реалии соответствовали ожиданиям', 'все твои родные были здоровы', 'ты никогда не болел(а)', 
                                'здоровье было крепким и денег было достаточно', 'трудности тебя обходили стороной', 'в сердце не было зимы', 
                                'в сердце была весна', 'в сердце было лето', 'было меньше дней холодных, злых людей', 
                                'аромат мандаринов ещё долго сохранял атмосферу праздника', 'всё, что мы отдали, вернулось нам втройне', 
                                'чтобы все твои мечты сбылись'])
    year_wish = random.choice(['запоминающимся', 'ярким', 'удачным', 'добрым', 'денежным', 'тёплым', 'счастливым', 'прекрасным', 
                               'изумительным', 'красочным', 'самым', 'лучшим', 'сочным', 'сытным', 'душевным', 'волшебным', 'сказочным', 
                               'успешным', 'незабываемым', 'вдохновляющим', 'неповторимым'])


    congrat_message = f'{greeting} {user}!'
    congrat_message += f'Этот год был {year_desc}, но {conjunction} он был и {year_positive}. {appreciation}!'
    congrat_message += f'{heartfelt} поздравляю тебя с праздником! Пусть {wishes}! Желаю тебе, чтобы {aspirations}, а новый год стал самым {year_wish}!'
    congrat_message += f'С новым счастьем!'


    return congrat_message


def slow_print(ascii_art, speed_ranges):
    lines = ascii_art.splitlines()
    total_lines = len(lines)

    for i, line in enumerate(lines):
        delay_range = (0.5, 0.5)
        for start, end, min_delay, max_delay in speed_ranges:
            if start <= i < end:
                delay_range = (min_delay, max_delay)
                break
        delay = random.uniform(*delay_range)
        progress = int(((i + 1) / total_lines) * 100)
        print(line)
        print(f"Loading= {progress}%", end="\r", flush=True)
        time.sleep(delay)
        print(" " * len(f"Loading= {progress}%"), end="\r", flush=True)

ascii_art = """
..:...:...:......:.......:...:...:...:..............:...:...:...:......:.......:...:...:  
.:-.::-.::-..:::.:::.:::.-.::-.::-.:..       .     ..::.-::.-::.-:::::::::::::.-::.-::.-  
.::.:::.:::..:::.:::.:::.-.:::.:..   ....:::.:::.:...  .::.:::.::::.:::.:::.:.:::.:::.::  
..:.:.:.:.:..::..::..::..:.:.:..   ..::..::.......:..:.  :.:.:.:.:..::..::..:::.:.:.:.:.  
.:-.::-.::-.::::.:::.:::.-.:::   .::.. .  . ...      ..:. ::.:::.-.::-.::-.::-:.:::.:::.  
..:.:.:.:.:..::..::..::..-.:.   .:.    ..   . .  ...... .: ..:::::.:::.:::.::::.:::.::..  
..:.:.:.:::..::..::..::..-.:   .:.          :..     . .. ...:.::::.::..:::.::.::.:::.:.   
.:-.::-.::-.:-::.-::.-::.-..  .:             :..      :   .::.::::-.::-.::-.::::.:::.:    
.:-.::-.::-.::::..::.:::.-..  ..       .. .  :.           .-.::-:.:::.:::.::::-.::-.::    
..:.:.:.:.:..::...:..::..:..         . .   :    .    .    ..:.:..::..::..::..:.:.:.:.:    
.:-.::-.::-..:::..::.:::.-..               . ..            .:::.-:::::::::::::.:::.:::.   
.::.:::.:::..:::..::.:::.-.   .   :.:....:.... ..::....:    :::.::::::::::::::.:::.:::..  
..:.:.:.:.:..::...:..::..-.       :::.-.:::...:..::..:::    ..::.::.:::.:::.::::.:::.::   
.::.:::.:::..:::..::.:::.:.       .::.:::::::::..:::.::    .:.::::::::::::::::::.:::.::   
..:.:.:.:.:..::...:..::..:.        .:..:.:.:.:.:.:.:...    .::.:::.:.:.:.:.:..:::.:::.:   
.:-.::-.::-.::::..::.:::.-.         ..::::.::...::::.      .:::.-:::::::::::::.:::.:::.   
..:.:.:.:.:..::...:..::..-          .. .:.:.:.:.:.        ..:.:.::::.:::.:::.:.:.:.:.:    
..:.:.:.:.:..::...:..::..:         .... ....:.. .         ..:.:.:..::..::..::..:.:.:..    
.:-.::-.::-.:-::..::.:::.           .:.:-.:::.:::          :::.::::-.::-.::-.::::.:::.    
.:-:::-:::-::-:::.:::-:          ...-:..:.:.: ..-.          :::-::-:::-:::-:::-:::-:::    
..:.:.:.:.:..::..........:.    ..:.:.:..::..:...::...           :.:.:.:.:.:.:..::..::..:  
.:-.::-.::-..:. .:::.:::.-.:.: . ....:..::...::.::..:...:.::-.::-:.::..:...::.:-:::-.::-  
.::.:::.:::..  .......:.......... .. .::...:...:....:...:.... ......:.:...:::..:::.:::.:  
..:.:.:.:.:              .:  .:.. . . ........:..:...:.  .  .:..:.... .. ...:..::..::...  
.:-.::-.::             ...:.:::..          .         .    .   ...::::: ....:::::::::::    
..:.:.:.:..               .       . .......  .   .. .:        .     . .  ....:.:.:....    
.:-.::-.::.                 ......:.:......:..           .   .      ... .::.:::::::..     
..:.:.:.:..            ..::.:::.:::.:::..::..::. ...::.:::.:::.:::.....  .. ..:::.:::..   
..:.:.:.:..          :.:.:..::..::..::..:.:.:.:.:...:..::..::..:.:.:.:.:..    .:.:.:.:.   
.:-.::-.::.        .-::.::::-.::-.::-.:-::.:::.-::...::-.::-.::-:.:::.:::.-:.. ::.:::.:   
.:-.::-.::.       ::-.:::...:..:...:::.-.::-.::-.:::  :::.:::.::::-.::-.::-.:::. :::.::   
.:-.::-.::      ..::-.: :......:::..::.-.::-.::-.::- .:::.:::.::::-.::-.::-.:......:.::   
..:.:.:.:.      :.:.:.... . .  .:.:.:..::..::..::..- ..:.:.:.:.:..::..::..::. ... . ..:   
.::.:::.::     .:..::. ::...  .::::::::::.:::.:::.::..::::::::::.:::.:::.:::.:::. ....:.  
..:.:.:.:.      :..::. .:..:.:.:.:.:.:::..::..::..:. .:.:.:.:.:..::..::..::..:.:.:   ...  
.:-.::-.::     .::.:::.::::-.::-.::-.::::.:::.:::.: ..-::.-::.-:::::::::::::::::.-::..:.  
.::.:::.::      :.:::.:::..:::.:::.:::::.:::.:::..   .::.:::.:::..:::.:::.:::::.:::. .:   
..:.:.:.:.       .:.:.:.:..::..::..::..:.:.:.:.  . .   :.:.:.:.:..::..::..::..:.:.: ..:   
.:-.::-.:          .:::.::::::::::::::.:::.:.  .:. -::.  .:::::::.:::.:::.:::.:::.: :::   
..:.:.:.:.            :..-.:.:.:.:.:.:...   .:..: ..:.:..  .:.:.:..::..::..::..:.. :.:.   
.:-.::-.::                ........ . ..::.:::.:: .::::-.:::.  ...:::.-::.::....:: .:::    
.:-.::-.::.            .    ..  ::.:::.-.::-.::-.::-:.:::.:::.....   ....  .::-...-.:     
.:-.::-.:::           .     ..:: .:::.-.::-.::-.::-:.:::.:::..::.:      . .:::..::-.      
 .:...... .              . ..:.:.:.:.:..::..::...:..:.:.:.:.:.:.:.           . .....      
                     .:.::::.:::.:::.:::::.::: ..:::::.:::.:::.::.          .....         
                    .::..:.:.:.:.:.:.:..::..:.  ::..:.:.:.:.:.:.:...                      
                   .:-:::-::::..::::::::-:::-::.-::::::::::::::::::-.                     
                  .:::::::.:::...:.:::.::::::::::::::.:::.:::.:::::::.                    
                ..:.:.:.:..::......::.::.:.:.:.:.:.:..::..::..::..:.:..                   
              .::::::::::::.:::.....::::::::::::::::::.:::..::.:::::::::                  
            .:.:::.:::.:::..::..::...:.::.:::.:::.:::..::..::..:::::.:.:..                
          ..-.:.:.:.:.:.:..:::.:::.::  :.:.:.:.:.:.::.:...:::.::..:.:...:.:..             
        .:.::::.:::.:::.:::...::-.::-.::...:::.:::.-.::-.::-.::-:.:...:::.::::.           
        :::.-.::-.::-.::-:.::..:::.::::-.::-.:.:.::-:.:::.:::.:... .::-.::-.::::          
       .::..:.:.:.:.:.:.:..:: .   .::..:.:........   .::..::......:.:.:.:.:.:::... .      
      ::-.::-:.:::.:::.::.:-.:::... .::. .:.:.:::.:  .  ..-.. :..:::.:::.:::.-.::-.       
      :::.::-:.:::.:::.::.::.:::...:     .:::::::..: ..:   ...::::::.:::.:::.:::::.       
      ..:::.-.:::.:::.:::..:::.::: :.  . . ::..::..:.. :.. :.:.:..::..::..::..:.:..       
       .::.::::.:::.:::.:.:::.:::..:.  .. ..:..::.::.. :.. :::.:.:::.:::.:::..:..         
           :.::.:::.:::.:.:.:.:.:.    .... .:.:.:.:...  .   ::.:.:.:.:.:.:.:.             
              . ..:.:::.:::..::....:. ...:.:.:::.::..... . ....:::..::...                 
                     .   ......:::.:. . .. :.:.:.:........ ..:..:.. .                     
                       ...:.:.:.:.:..  ......:...::..: . .  .:.:::..::...                 
                     .-.::::.:::.:::..:......-...-.::::.. .. .:.-.::-.::-..               
                    :-:::-:::-:::-:::.:.: ...-::..::-:::-. .::  -:::-:::-::.              
                   ..::..:.:.:.:.:.:.  ..    ..:.: .::..:.. ....  ..:.:.:.:..             
                    .:::.-.::-.::-.::. .:. .....:::...::-.:::. .:......:::.::             
         .. .. . ...  .:.-.:::.:::.:::.  :.  .......:.:.:.:::.:... :....::.::.  :..::..   
          ...:::.::...  .:.:.:.:.:.:.:... . ... : ........:.:.:...  ..:. .::.  .:..::..   
              .........    ..::::::::::... .:::.....::..::.::::::.  ....  ...:.:::.::.    
                                  .   .. . ..:......::...:....           . ..:.:::...     
                                         .:::-. .::::. ..   .::.-:::::.. ...:::::.        
                                         ....::.   ...   .:..::..:.:.:...       .:        
                                          :.:.:.:.     .:.:   ...::..::..::   ...:        
                                           .:.-:..:.  ..:...::-.:-::.-::.-::.-.::-        
                                             ::: . .. ::..:::.::::-.:::.:.:.::: .:        
                                               .. .:  ...:.:::.::::-.. :.::-... ..        
                                                  .   : .::..::..:.:  ...::..: ..         
                                                       ..:::.:::.:::. ::..:.              

"""

speed_ranges = [
    (0, 26, 0.1, 0.3),
    (26, 31, 1, 3),
    (31, 48, 0.1, 0.3),
    (48, 50, 3, 10),
    (50, 74, 0.05, 0.1)
]


slow_print(ascii_art, speed_ranges)
print("""                                                         .::..                            
              .::.:....::::.                        .=+*######*=                          
          .::.              .:::                 :=*############*.                        
        ::                      ::           -+*#################=                        
       -               .          -.           .=######**++++*#####*+=:                   
      -.    -=:=- *+   *-::-:      -          :=###*+----------+*#######+:                
      :.    -=.:-+-+:  + *+-+      -        .=-=*=---------------=*#######+.              
       -                          -       :-------=---------------=#########=             
        ::                      ::        --+:::::=---------------=##########+            
          .::..               :.          :.-     :   +:    :=----*###########=           
               .:.....:.     -            --------=:.       :=----#############           
                       .::.. .:         :------------=-----------=##*##########.          
    ::.                    ..::-.     .:-==---------==------------##-=#########.          
  .=-----:                          :-----------------------------=*--###+*###*           
   ---------:.                     .------------------------++===-----++==-*##=           
    .:----------:.                   ..:::::::--::==:.-*+--*@@@@@@%*------=##*            
      -=======------::.                          --@@@@@@@@@@@@@@@@@#--######.            
     .+--==--------------::                  .::.==#%%%@@@@@@@@@@@@@#-*#####-             
    :---==----=---------------::.    .:-::. ---------:::=-=****##%#+--#####*              
    .=---====-====-----------------:=++++=====-=---------------------+#*###+              
      ::--=----------------------------=+=====+++------------------=+====*#*              
           .:-=-------------------------=+==++++=++===--------====++======+*:             
                  ..::------------------+==+=++=======++++++++===++=====+++==+=:          
                          .::-----------+=+=++==================++=====++========-        
                                =++====+=+==+===================+=====+============-      
                                .==++++=+==+===================+======+==============     
                                  .--==+===+===================+=====+=========+++++==    
                                       ===+==+++++++++========+======+====++===-----*=    
                                      -=++===========+========*=======+=++-----------:    
                                      ++======================+=======+++*-----------=.   
                                     .*======================+============+-----------=   
                                     ========================+=============+------------  
                                    -+=======================+==============+------=---=. 
""")
time.sleep(3)
print(generate_text())
time.sleep(15)
print("Our website")
print("""                                                                                                                                                       
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
              .+++++++++++++++++++++++++.   ++++++++++++++++++.          -+++++++++++++++++++++.   +++-       +++++++++++++++++++++++++:              
              -@@@@@@@@@@@@@@@@@@@@@@@@@-   @@@@@@@@@@@@@@@@@@-          *@@@@@@@@@@@@@@@@@@@@@-   @@@*       @@@@@@@@@@@@@@@@@@@@@@@@@=              
              -@@@+.................=@@@-   @@@#.......@@@#...    ###+   ....@@@#.......@@@@@@@%###@@@*       @@@#..................@@@=              
              -@@@=                 -@@@-   @@@*       @@@*       @@@*       @@@*       @@@@@@@@@@@@@@*       @@@*                  @@@=              
              -@@@=   @@@@@@@@@@@   -@@@-          *@@@@@@@@@@@@@@@@@*              *@@@@@@*       @@@*       @@@*   *@@@@@@@@@@-   @@@=              
              -@@@=   @@@@@@@@@@@   -@@@-   ....   +%%%@@@@%%%%%%%%%%*...    .......*%%%@@@*       %%%+       @@@*   *@@@@@@@@@@-   @@@=              
              -@@@=   @@@@@@@@@@@   -@@@-   @@@*       @@@*          -@@@-   @@@@@@@-   @@@*                  @@@*   *@@@@@@@@@@-   @@@=              
              -@@@=   @@@@@@@@@@@   -@@@-   ***=       ***+---.      :***=---@@@@@@@+---@@@*   :---           @@@*   *@@@@@@@@@@-   @@@=              
              -@@@=   @@@@@@@@@@@   -@@@-                 -@@@-          *@@@@@@@@@@@@@@@@@*   *@@@           @@@*   *@@@@@@@@@@-   @@@=              
              -@@@=   +++++++++++   -@@@-              ---+@@@+----------#@@@+++#@@@@@@@@@@*   -+++   .---.   @@@*   -++++++++++.   @@@=              
              -@@@=                 -@@@-              @@@@@@@@@@@@@@@@@@@@@@   -@@@@@@@@@@*          -@@@-   @@@*                  @@@=              
              -@@@#+++++++++++++++++#@@@-   +++-   -+++---+@@@+---@@@#---#@@@   -@@@+---@@@*   -+++   -@@@-   @@@%++++++++++++++++++@@@=              
              -@@@@@@@@@@@@@@@@@@@@@@@@@-   @@@*   *@@@   -@@@-   @@@*   *@@@   -@@@-   @@@*   *@@@   -@@@-   @@@@@@@@@@@@@@@@@@@@@@@@@=              
               .........................    @@@@###-...    ...    @@@@###@@@@###%@@@-   ....   *@@@   -@@@-   .........................               
                                            @@@@@@@-              @@@@@@@@@@@@@@@@@@-          *@@@   -@@@-                                           
              -@@@=   @@@@@@@-   @@@@@@@@@@@   -@@@@@@@   -@@@-      -@@@-   @@@@@@@@@@@   -@@@@@@@           @@@*       @@@*   *@@@@@@=              
              :%%%=...%%%%@@@-   @@@@%%%%%%%   -@@@%%%%...-%%%-......-%%%:   %%%%@@@@@@@...=@@@%%%%....       @@@#...    @@@#...*%%%@@@=              
                  =@@@   -@@@-   @@@*          -@@@-   @@@*   *@@@@@@*          -@@@@@@@@@@@@@@-   @@@*       @@@@@@@-   @@@@@@@-   @@@=              
              .---=***   :***:   @@@#---.   ---=***=---***=   *@@@***=   :---   :**************:   @@@#---.   @@@@@@@+---@@@%***=---@@@=              
              -@@@=              @@@@@@@-   @@@*   *@@@       *@@@       *@@@                      @@@@@@@-   @@@@@@@@@@@@@@*   *@@@@@@=              
              .==============.   @@@%=======@@@%===%@@@===-   -===   .===%@@@       -===       -======*@@@-   @@@@@@@*===@@@*   *@@@===:              
                  =@@@@@@@@@@-   @@@*   *@@@@@@@@@@@@@@@@@*          -@@@@@@@       *@@@       *@@@   -@@@-   @@@@@@@-   @@@*   *@@@                  
              :***=----------.   @@@%***%@@@@@@#----------:       ***#@@@@@@@***=   *@@@       *@@@   .---.   -------+***@@@*   :---                  
              -@@@=              @@@@@@@@@@@@@@*                  @@@@@@@@@@@@@@*   *@@@       *@@@                  *@@@@@@*                         
              -@@@=   ###+       ...........@@@@#######   :###:   @@@#...........   *@@@   :###-...       +###       ....@@@*   +###                  
              -@@@=   @@@*                  @@@@@@@@@@@   -@@@-   @@@*              *@@@   -@@@-          *@@@           @@@*   *@@@                  
              -@@@=   @@@*          -@@@-   @@@*   *@@@@@@*       @@@*       @@@@@@@@@@@@@@@@@@-      -@@@-   @@@@@@@-      -@@@-                     
              -@@@=   %%%+       ...-%%%-...@@@*   +%%%@@@*   ....%%%*...    %%%%%%%@@@@%%%%@@@-      -@@@=...@@@@@@@-      -@@@-                     
              -@@@=              @@@*   *@@@@@@*       @@@*   *@@@   -@@@-          *@@@   -@@@-      -@@@@@@@@@@@@@@-      -@@@-                     
              :***-          :---***+---+***@@@#-------@@@*   =***---=***:          =***---+@@@+------+@@@@@@@@@@%***=---   -@@@-                     
                             *@@@   -@@@-   @@@@@@@@@@@@@@*       @@@*                  @@@@@@@@@@@@@@@@@@@@@@@@@*   *@@@   -@@@-                     
              .===:   ===-   *@@@===========@@@%==============.   @@@%===.              @@@%=======@@@@@@@*===@@@*   *@@@=======.   ===:              
              -@@@=   @@@*   *@@@@@@*   *@@@@@@*          -@@@-   @@@@@@@-              @@@*       @@@@@@@-   @@@*   *@@@@@@*       @@@=              
              -@@@=   @@@*   *@@@@@@%***=---@@@%**********#@@@#***---+@@@#******=       ---=***:   ---+@@@-   @@@%***%@@@---=***:   ---.              
              -@@@=   @@@*   *@@@@@@@@@@-   @@@@@@@@@@@@@@@@@@@@@@   -@@@@@@@@@@*          -@@@-      -@@@-   @@@@@@@@@@@   -@@@-                     
               ...    ....   *@@@.......*%%%.......#@@@...=@@@=...   -@@@=...@@@*   +%%%    ...*%%%%%%%@@@-   @@@#...#@@@    ...                      
                             *@@@       *@@@       *@@@   -@@@-      -@@@-   @@@*   *@@@       *@@@@@@@@@@-   @@@*   *@@@                             
              -@@@@@@@@@@@@@@-   @@@@@@@-   @@@*   *@@@   -@@@-   @@@*   *@@@@@@*   *@@@@@@@@@@@@@@   -@@@@@@@   -@@@-   @@@@@@@@@@@                  
              :###%@@@###%@@@=...#######:   ###+...+###...-###-...@@@#...#@@@@@@*   *@@@###%@@@@@@@...=@@@@@@@...=@@@-   ###%@@@%###...               
                  =@@@   -@@@@@@@              -@@@-   @@@*   *@@@@@@@@@@@@@@@@@*   *@@@   -@@@@@@@@@@@@@@@@@@@@@@@@@-      -@@@-   @@@=              
              .---*@@@---=***%@@@   .---.      :***:   ***=   *@@@@@@@@@@#******+---+***---+@@@#***@@@%*******@@@%***:      :***=---@@@=              
              -@@@@@@@@@@*   *@@@   -@@@-                     *@@@@@@@@@@-      -@@@-   @@@@@@@-   @@@*       @@@*              *@@@@@@=              
              -@@@#======-   -===   .===.   ==================%@@@@@@@@@@-      -@@@-   ==============-   -===@@@%==========-   -======:              
              -@@@=                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@-      -@@@-          *@@@       *@@@@@@@@@@@@@@@@@*                         
              .---=**********:      :***:   -------#@@@---+@@@@@@@@@@#---.   ***+---.   ***=   *@@@   :***%@@@@@@@@@@@@@@---:       ***-              
                  =@@@@@@@@@@-      -@@@-          *@@@   -@@@@@@@@@@*       @@@*       @@@*   *@@@   -@@@@@@@@@@@@@@@@@@           @@@=              
                   ..........        ...    %%%%%%%@@@@%%%%@@@@@@@@@@@%%%%%%%@@@*   +%%%....   *@@@   -@@@=..........#@@@%%%+   +%%%...               
                                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*   *@@@       *@@@   -@@@-          *@@@@@@*   *@@@                  
              -@@@@@@@@@@@@@@@@@@@@@@@@@-   @@@*          -@@@@@@@@@@*   *@@@   -@@@@@@@@@@*       @@@@@@@-   @@@*   *@@@       *@@@                  
              -@@@%#################%@@@-   @@@#.......   -@@@@@@@###+   *@@@   -@@@@@@@@@@#...    @@@@@@@-   ###+   *@@@.......+###...               
              -@@@=                 -@@@-   @@@@@@@@@@@   -@@@@@@@       *@@@   -@@@@@@@@@@@@@@-   @@@@@@@-          *@@@@@@@@@@-   @@@=              
              -@@@=   -----------   -@@@-   +++++++%@@@---=+++++++       -+++   .+++%@@@@@@@@@@-   @@@@@@@+----------#@@@+++#@@@+---@@@=              
              -@@@=   @@@@@@@@@@@   -@@@-          *@@@@@@*                         *@@@@@@@@@@-   @@@@@@@@@@@@@@@@@@@@@@   -@@@@@@@@@@=              
              -@@@=   @@@@@@@@@@@   -@@@-   +++-   *@@@---=+++++++       -+++       :---@@@#---.   @@@#----------+@@@+---++++-------@@@=              
              -@@@=   @@@@@@@@@@@   -@@@-   @@@*   *@@@   -@@@@@@@       *@@@           @@@*       @@@*          -@@@-   @@@*       @@@=              
              -@@@=   @@@@@@@@@@@   -@@@-   @@@%***=---   .---#@@@*******%@@@*******:   ---=*******@@@%**********#@@@-   ---=***:   ---.              
              -@@@=   @@@@@@@@@@@   -@@@-   @@@@@@@-          *@@@@@@@@@@@@@@@@@@@@@-      -@@@@@@@@@@@@@@@@@@@@@@@@@-      -@@@-                     
              -@@@=   ...........   -@@@-   .......           *@@@...=@@@@@@@@@@@@@@-       ...#@@@...=@@@=......=@@@%%%%%%%*...    %%%=              
              -@@@=                 -@@@-                     *@@@   -@@@@@@@@@@@@@@-          *@@@   -@@@-      -@@@@@@@@@@*       @@@=              
              -@@@@@@@@@@@@@@@@@@@@@@@@@-   @@@@@@@@@@@   -@@@-      -@@@-   @@@*   *@@@   -@@@@@@@                  *@@@@@@@@@@-                     
              :#########################:   ###########   :###:      :###:   ###+   +###   :#######                  +##########:                     
                                                                                                                                                      
                                                                                                                                                      
 """)                                                                                                                                                     
input()                                                                                                                                                    
                                                                                                                                                      
                                                                                                                                                      
                                                                                                                                                      
