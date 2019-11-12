# Card Game 3 And 2.
## `We will create a card game call 3 and 2 in python.`

>## `NOTE`
>We created several files, where we created classes and some methods, before we put it all in the main file.
>We thought to import the files into the developers file, but due to problems with the import, we decided to merge everything into the developers file.

>## `Three And Two Game.`

>1. [Instruction](#Instruction)
>1. [Use Of Colorama](#Use-of-Colorama)
>1. [Download and installation](#Download-and-installation)
>1. [Example](#Example)
>1. [Story Of Tres Y Dos](#Story-Of-Tres-Y-Dos)
>1. [Introduction](#Introduction)
>1. [Objective](#Objective)
>1. [Players and Cards](#Players-and-Cards)
>1. [Deal](#Deal)
>1. [Play](#Play)
>1. [End of Game](#End-of-Game)
>1. [Bibliography](#Bibliography)

>## `Instruction`
>To compile the game it is necessary to have downloaded python (3.7). 
>Similarly, [colorama](#Use-of-Colorama) (Library of colors reserved in python).
>You must open the main file and run it to start the game, you are asked to enter the names and surnames of the players and the decks of each will be created.
>When starting the game a card will appear automatically and you will have 2 options: the first to keep the card shown or the second to throw the same card.
>In the following rounds you can choose whether you want a new card from the middle deck by typing the number "1" or the card that appears in the discard deck by typing the number "2". The card you have chosen will be added to your deck and you choose which of the 6 cards you want to replace it (counting from 0 to 5), this will happen around the entire game until one of the players fulfills the objective of the game; get 3 cards of the same value and similarly 2 other cards, but with a value different from the remaining 3, The game ends with a "You Win" sign.

>## `Use of Colorama`
>You can implement colored text and background on the console.
>Colorama is a module that allows you to print colored text in the output of the terminal or console, including the background or style of the text, on multiple platforms.
>

>## `Download and installation`
>Colorama no tiene dependencias y está escrito completamente en Python, por lo que su instalación es muy sencilla. Puedes descargar el código de fuente en archivo ZIP desde su página en [PyPI](https://pypi.org/project/colorama/#downloads). Una vez extraído, simplemente:
>
>python setup.py install
>
>Microsoft Windows users can alternatively download an installer from the module via windows.recursospython.com.
>

>## `Example`
>Before printing any text, it is necessary to initialize colorama.
>
>1. import colorama
>2. from colorama import Fore
>
>To change the color of the text, one of the colorama constants is used. Fore. *. For example, the following code prints "Python Resources" in green.
>
>1. from colorama import Fore, init
>2. init()
>3.
>4. print(Fore.GREEN + "Recursos Python")


>## `Story Of Tres Y Dos`
>## `Introduction`
>Tres y dos (Spanish for 'three and two') is a simple draw and discard game of the rummy type played in the Dominican Republic. It would be interesting to know whether it is played in other Spanish speaking countries. At present we do not know any players from elsewhere so it may be that it originates from the Dominican Republic.

>## `Objective`
>The object is to be the first player to form in their hand a "full house": one triplet of 3 matching cards and one pair of 2 matching cards, such as K-K-K-8-8 or 3-3-3-5-5 (thus the name tres y dos), through the process of draw and discard.

>## `Players and Cards`
>A standard 52 card deck without Jokers is used. Anywhere from 2 to around 7 players can play, but is perhaps best for 3 to 5 players. The cards have no ranking order and the suits have no significance. The ranks are merely used for matching purposes. Two or more cards of the same rank are considered to match.

>## `Deal`
>The dealer may be chosen at random. Standard procedure is for the dealer to shuffle the cards and pass the deck to the player to the dealer's left to cut. The dealer then deals the cards to the players one at a time in counter clockwise order, starting with the player to the dealer's right, until each player receives 5 cards. The remaining cards are placed in a stack face down to form the stock. The top card of the stock is turned over and placed face up next to the stock to start the discard pile. Cards in the discard pile are to be face up in a single stack so that only the topmost card can be seen.

>## `Play`
>The player to the dealer's right plays first. During each turn a player must:
>
>First draw one card - either the top card of the stock or the top card of the discard pile - and add it to his or her hand.
>Then discard one of his or her six cards, placing it face up on the discard pile.
>If you draw a card from the discard pile, you are not allowed to discard the same card back to the discard pile in the same turn. This would be an effective pass, and passing is not allowed. You are, however, allowed to discard a card you have just drawn from the stock, or a card you took from the discard pile in a previous turn.
>
>A turn is over after the player has discarded. Turn to play then passes to the right - to the next player in counter clockwise order.
>
>If the stock becomes empty, all its cards having been drawn, players keep playing their turns until someone wants to draw from the stock. Once this happens the dealer picks up the discard pile, shuffles it, and places it face down to form a new stock. The player who wished to draw from the stock must now do so, then discard a card, starting a new discard pile in the process. The game then continues as usual.

>## `End of Game`
>A player who forms tres y dos (a full house - see objective) may place his or her hand face up on the playing surface for all the other players to see. The game ends immediately and this player is the winner. The first player to show a winning hand is the winner, no matter if he or she was dealt a winning hand before anyone took a turn or if another player or players have winning hands but do not notice. In the case that a player shows his or her hand but it is not a winning hand, this player takes back their hand and play continues as usual.
>
>On rare occasions more than one player may try to show a winning hand at the same time. For example this could occur if two players were dealt a full house as their initial hand. If it is not possible to agree who showed first, the winner is the player among those who showed winning hands whose turn would have come first, starting with the player to dealer's right and going around anticlockwise, with the dealer considered last.

>## `ALL THIS INFORMATION FROM HUMBERNIO LOCKWARD.`


>## `Bibliography`
https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

https://www.youtube.com/watch?v=yXY3f9jw7fg&t=314s

https://www.pagat.com/rummy/tresydos.html

https://docs.python.org/2/library/time.html#time.sleep

https://recursospython.com/guias-y-manuales/colorama-texto-fondo-coloreados-la-consola/