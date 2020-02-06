import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.common.keys import Keys

url = "https://top.pons.me/?dict=frpl"

text = """
<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <meta charset="utf-8" />
  <title>Top</title>
</head>
<body>
<h2>Stats for Tue, 21 Jan 2020 20:47:21 +0100</h2><h3>frpl - fr - keyword-all (last 1h)</h3>
33: fondre<br />
15: Real | mettre<br />
14: Endorr<br />
12: Deviendre | Endorter<br />
11: devoir | donner | faire | jamais<br />
10: Aktualnia | Pprcine | contrecoup | cultiver | cultivé | donné | donnée | venir<br />
9: Chodzimy | L'apport | Pay-Bas | Ssij | endormir | partir | vouloir<br />
8:  (...16 more)<br />
<h3>frpl - fr - keyword-all (last 24h)</h3>
101: devoir<br />
93: voir<br />
84: être<br />
72: faire | pouvoir<br />
34: dire<br />
32: connaître<br />
31: mesurer<br />
30: boire<br />
29: revenir<br />
28: descendre | mais<br />
25: étudier<br />
23: moins<br />
22: prochain<br />
20: entreprendre<br />
18: coucher | surtout<br />
17: coucou | penser<br />
15: maîtriser<br />
14: Furnir | manger | soulager<br />
13: rhumer (...2 more)<br />
<h3>frpl - pl - keyword-all (last 1h)</h3>
16: Kiedykolwiek<br />
15: Chodzimy<br />
13: Odbierać<br />
12: Nieważny | Ważny<br />
10: zbierać<br />
9: Bakalia | Conciliat | L'apport | Oliwka | Pay-Bas | Ssij | przykryć | tempérance<br />
8: Dejaneur | Kulturę | Marmelle | Pénien | Real | Winogrono | piner | prysznic | przeprawa | zabierać<br />
7: Tylko (...10 more)<br />
<h3>frpl - pl - keyword-all (last 24h)</h3>
49: tłumacz<br />
29: tak<br />
28: Horsirr<br />
25: dobranoc<br />
24: praca<br />
22: zbierać<br />
21: petarda | wracać<br />
20: tylko<br />
19: język<br />
18: cześć | lubić<br />
17: wycieraczka<br />
16: ale | baba | krótki | wychodzić<br />
15: Wysoki | dużo | hatier | mądry | skąpy | wiara | zawierać<br />
14: suszarka (...5 more)<br />
<h3>frpl - unknown - keyword-all (last 1h)</h3>
1: aimes-les-t-il? | ettiohc<br />
<h3>frpl - unknown - keyword-all (last 24h)</h3>
7: L'ECRAIL3 | Reine-claude<br />
6: 176<br />
5: Rejaill<br />
2: na'treasure | {searchTerms}<br />
1: Aper%EF%BF%BDoit | aimes-les-t-il? | dachówkaznaczyć | dbałość | einezsołgz | ersatzneubau | erttemo | ettiohc | general.invoices.return.to.supplier.of.items | gewohnheit | intangiblrefouler | recalcitratans | reine-claude | selbstredend | thighs | watfairefoute | zurückgeben | ćahcpyw | مقبرة (...7 more)<br />
<h3>frpl - fr - keyword-nomatch (last 1h)</h3>
14: Endorr<br />
12: Deviendre | Endorter<br />
10: <br />
9: <br />
8: Real<br />
7: <br />
4: Chamaill<br />
2: Zakupy | aimes-les-t-il? | désarroi | fenir | zatem<br />
1: debarasser | effectuesement | kurwa | louvre | opadnięcie | opracowanie | pejcz | piramide | płaczesz | reveni | szansa (...137 more)<br />
<h3>frpl - fr - keyword-nomatch (last 24h)</h3>
15: Juoe | Pagues | Radicalisation<br />
14: Endorr | Entrepise | Furnir | acquiser<br />
13: Augentation | Exergue | Natłok | Raffinement | S'entender | aduste | malkontent | veneres<br />
12: Chaudronnier | Deviendre | Endorter | Insilente | Moim | Zaleta<br />
11: Embraqyer | Rane | Supplanter (...8 more)<br />
<h3>frpl - pl - keyword-nomatch (last 1h)</h3>
13: Chodzimy<br />
9: Bakalia | tempérance<br />
7:  |<br />
6: Conciliant<br />
2: Andrzej<br />
1: Efrpl22063557 | G&#45;dur | accélérez | avoir | bus | crapaud | eaux | gluten | java | mais | pej | pozyskiwanie | souffrir | spedytor | usg | vont (...70 more)<br />
<h3>frpl - pl - keyword-nomatch (last 24h)</h3>
18: Owic<br />
15: stawy<br />
14: <br />
13: Ansi | Powiernictwo<br />
12: Bullet | Chodować | Zwany<br />
11: GMO | Kreować | Merci<br />
10: Kamiennice | Nielubiany | Pesto | Torcida | apaisement<br />
9: Envoient | Habitait | Ogm | Położona | Wygidne | ronceaux | tempérance (...4 more)<br />
<h3>frpl - unknown - keyword-nomatch (last 1h)</h3>
10: Pprcine<br />
9: L'apport | Pay-Bas | Real | Ssij<br />
8: Contonte | Dejaneur | Guéguerre | Immerssion | Marmelle | piner | przykryć<br />
7: Pénien | Wspierany<br />
6: Motywujacy | Souk<br />
5: Attendee | L’ail | Nondir | randonner<br />
3: miséricorde<br />
2: Pantofle | intern (...6 more)<br />
<h3>frpl - unknown - keyword-nomatch (last 24h)</h3>
28: Horsirr<br />
21: Ecler<br />
15: Proliferer | hatier<br />
14: Rectum<br />
13: torque<br />
12: Copaon | Fonchon | Propension | Veillesse | courroucer | veneres<br />
11: Apercoit | Attentisme | Feuile | Pation | Poucl | S'eparer | Veilleise | anoblir | encor<br />
10: Rozbawiony | Torque | aligoté | besson (...23 more)<br />
<h3>frpl - fr - phrase-all (last 1h)</h3>
14: Juste place<br />
9: A la toute vitesse | Se endorter<br />
8: Meurs de faun | Pay Bas | Pay bas | Pies przewodnik<br />
7: Faire en sorte que | L'apport nouveau | Peste porcine | la carte<br />
6: Emploi de temps<br />
5: co tam | comme ci comme ca<br />
4: A la toute vitrsse | Continuer jusqu’a | Les principaux | Mouth ulcer | ange ou demon | dodawać do | sela vie | si cala fon | vers sept heures | wszystkiego najlepszego<br />
3: conditioner apres shampooing (...7 more)<br />
<h3>frpl - fr - phrase-all (last 24h)</h3>
72: comme ci comme ca<br />
37: si cala fon<br />
36: żeli papą<br />
27: comment sava | sela vie<br />
23: dzień dobry | la vie est belle<br />
22: enchanté mademoiselle<br />
19: nie ma za co<br />
18: au revoir | ca va | proszę bardzo<br />
16: maillon de corps<br />
15: Contre coeur | au chante | bon voyage | do widzenia<br />
14: Juste place | Niveau d huile correct | Par ce tempa gris<br />
13: Aimer pas do tout | De gouter | Jeux en ligne | Un boite | et voila (...4 more)<br />
<h3>frpl - pl - phrase-all (last 1h)</h3>
10: polsko francuski<br />
8: Pay Bas | Pay bas | Pies przewodnik<br />
7: slownik polsko francuski<br />
6: ja będę<br />
5: co tam<br />
4: Uprawiać sporty ekstremalne | wszystkiego najlepszego<br />
3: Cho cho | JE T AIME | Le bourg | Le bourgeois | Nie mogę znaleźć | Ssij Penis | Współczesna francja | comment ca va | sale gosse | uzupelnij diagram, wpisujac rzeczowniki zawierajace "u". | vidange a prevoir<br />
2: Słownik niemieckiego | Warsztaty z teatru japońskiego | sans doute | se lever | ty musiałaś zostać w szpitalu jeszcze przez około dwa tygodnie (...69 more)<br />
<h3>frpl - pl - phrase-all (last 24h)</h3>
66: slownik polsko francuski<br />
62: polsko francuski<br />
24: ça été ta journée<br />
23: dzień dobry<br />
18: au revoir | ca va | nie ma za co | proszę bardzo | si cala fon<br />
15: au chante | bon voyage<br />
14: Ramka na zdjęcia | Spędzać czas z rodziną | do widzenia<br />
13: JE T AIME | Mam kanał który nauczył mnie wiele | Na oonii | et voila<br />
12: Być odmiana | Na łonie przyrody | Ona Na wakacje jeździ do mamy | Spędzać czas z przyjaciółmi | Uczunie sie | kocham cię<br />
11: wszystkiego najlepszego (...6 more)<br />
<h3>frpl - unknown - phrase-all (last 1h)</h3>
2: Joyeuse fête, je vous souhaite beaucoup de bonheur d’amour et de santé.<br />
1: J'apprends maintenant | Je garde mon contrat chez pouicland car c'est un temps partiel à Paris, chez une architecte. Pour faire la même chose que chez brunerie. | Je vais continuer à venir un week-end sur deux et une fois par mois j'arriverai le mercredi soir alors j'espère continuer à te voir. Je pense fort à l'équipe. Ça va comment toi? | Mieszkam w Warszawie to jest głośne, ale spokojne miasto | Tout s'est précipité car je suis partie à Montréal début janvier. C'était le cadeau de mes parents et mon frère pour mes 40 ans... Pour aller le voir. Ça m'a fait du bien, prendre l'air frais, être seule là bas. Et j'ai pensé à toi... Je me suis dit que maintenant que j'avais testé les-24vdegres à Montréal, je pouvais partir en Pologne. | Wesołych świąt, życzę wam dużo szczęścia, miłości i zdrowia. | bardzo się o ciebie martwiłam | bonjour madame vous désirez | des sons comme en polonaise | jeszcze przez około dwa tygodnie | jeszcze przez około dwa tygodnir | niemiecki jest super | osiagnac sukces | panneau des departs | podroz statkiwn | powoli wracasz do zdrowia | radosna uczta | to był żart | ton frère m’a dit que tu devrais rester à l’hopital pendant environ deux semaines de plus | ton frère m’a dit que tu devrais rester à l’hopital pendant environ deux senaines de plus | ton frère m’a dit que tu devrais rester à l’hopital pour environ deux semaines de plus | twoj brat mowił mi | ty musiałaś zostać w szpitalu jeszcze przez około dwa tygodnie | veuillez croire à l’expression de mes sentiments les meilleurs (...10 more)<br />
<h3>frpl - unknown - phrase-all (last 24h)</h3>
2: jestem zadowolona z sukcesu paula | j’n’arrive pas a me dètendre | o czym Pani marzy | si je pouvais t'étrangler!  Je ferais ça | tarcza do pily | w dzisiejszych czasach<br />
1: 5 minut pózniej | Bonjour Karolina je suis navré d'annuler la course. Mon vol étant annulé je ne vais pas me rendre à l'aéroport. | Je garde mon contrat chez pouicland car c'est un temps partiel à Paris, chez une architecte. Pour faire la même chose que chez brunerie. | Moja mama bardzo lubi zwierzęta | Moja mama ma na imię Monika i ma 46 lat.Jest piękną kobietą.Ma krótkie włosy i niebieskie oczy.Jest kochaną mamą i zawsze pomaga innym.Jest z zawodu pielęgniarką.Bardzo lubi swoją prace. | Ser liberal, de acuerdo a mi escritura favorita, el diccionario Merriam-Webster, es ser de mente abierta, es estar libre de las restricciones del dogmatismo y la autoridad, es ser generosos y creer en la bondad básica de la humanidad. La religión suele definirse como aquello que nos vincula fuertemente a aquello de importancia última. Por lo tanto, los liberales religiosos son quienes están vinculados, a través de la generosidad y la apertura, a los aspectos más importantes de la vida. Y en ello yace el desafío. Si somos de mente abierta y no atados a la autoridad, ¿quién o qué decide aquellas cuestiones de importancia última?
Ministra unitaria universalista Kimi Riegel What is Liberal Religion?
Referencias[editar]
↑ What is Liberal Religion and Why Should I Care?: Sermón del Revdo. Patrick Price
Control de autoridades
Proyectos Wikimedia  Datos: Q4259813 | anna daje ksiazke noemie | co ty bierzesz na plażę | czy ma pani dreszcze | dans biem des circonatances | les boat prople | mężczyzna może dać ci pieniądze albo spermę, i to nie każdy | on ma katar | srapacz chmur | trudno przyzwyczaic sie do | w tym momencie uczę się francuskiego | wysłac przez poczte | znajduje sie na ulicy | zobaczyć się z kimś (...476 more)<br />
<h3>frpl - fr - phrase-nomatch (last 1h)</h3>
14: Juste place<br />
9: Se endorter<br />
4: ange ou demon | sela vie<br />
3: conditioner apres shampooing | si cala fon | vers sept heures<br />
2: Je en vais chanter a elle | Je vais continuer à venir un week-end sur deux et une fois par mois j'arriverai le mercredi soir alors j'espère continuer à te voir. Je pense fort à l'équipe. Ça va comment toi? | Przyszli do nas znajomi. Na kolacje jedliśmy klopsiki w sosie pieczarkowym i inne różne przekąski. Żeby uczcić ostatni dzień w roku piliśmy Whyski z colą. Tradycyjnie w telewizji oglądaliśmy sylwestrową moc przebojów. Graliśmy w różne gry planszowe. O północy wzięliśmy szampana i fajerwerki i poszliśmy na dwór przywitać nowy rok | Tu a qu'elle âge. | Un peu mal au dos.. Bises à johanna | bonjour madame, vous désirez? | chardon bleu | comment sava | des sons comme en polonaise | entre sept et huit heures | jeść chleb z niejednego pieca | merci google | pourquoi tu n'as pas le temps de me parler ?tu ne veux pas me parler ou quoi ? | sava bien | se sacher | veuillez croire à l’expression de mes sentiments les meilleurs | votre garage a effectué | 🤷‍♀qu est qui ses passé ???? (...5 more)<br />
<h3>frpl - fr - phrase-nomatch (last 24h)</h3>
36: żeli papą<br />
27: comment sava | sela vie<br />
23: si cala fon<br />
22: enchanté mademoiselle<br />
16: la vie est belle | maillon de corps<br />
14: Juste place | Niveau d huile correct | Par ce tempa gris<br />
13: Aimer pas do tout | De gouter | Jeux en ligne | Un boite<br />
12: Par ce temps | Vient de commencer<br />
11: Mettre au pr | se rend au coeur<br />
10: Bonsoir Monsieur Pavel tu sais bien que j'apprécie ton travail mais là tout le magasin et que poussière aussi bien les murs le bois tout, comment renettoyer tout ça ? Il fallait être là pour surveiller. Mourad | Ligne svelte | Wy jesteście<br />
9: Crotte de nez | Se endorter | film ERTYCZNY | se magnifique (...2 more)<br />
<h3>frpl - pl - phrase-nomatch (last 1h)</h3>
10: polsko francuski<br />
7: slownik polsko francuski<br />
6: ja będę<br />
3: Uprawiać sporty ekstremalne | uzupelnij diagram, wpisujac rzeczowniki zawierajace "u". | vidange a prevoir<br />
2: "Naszą nadzieją było dalsze służenie królowej, Wspólnocie Narodów i organizacjom wojskowym bez pobierania publicznych funduszy. | Chciałabym zapisać się na warsztaty z teatru japonskiego | Musze zajac sie corkami i ogladam film | Na warsztaty z teatru | Pielegniarki pracuja w nieuregulowanych godzinach, wiec czesto sa niewyspane | Przyszli do nas znajomi. Na kolacje jedliśmy klopsiki w sosie pieczarkowym i inne różne przekąski. Żeby uczcić ostatni dzień w roku piliśmy Whyski z colą. Tradycyjnie w telewizji oglądaliśmy sylwestrową moc przebojów. Graliśmy w różne gry planszowe. O północy wzięliśmy szampana i fajerwerki i poszliśmy na dwór przywitać nowy rok | Słownik niemieckiego | Tak poszli ale niemam teraz czasu odezwie sie pozniej ok | Warsztaty z teatru japońskiego | Zdaje się egzamin | Zdaje się maturę | ja ty on ona ono | powoli wracasz do zdrowia | stan faktyczny | to był żart | ty musiałaś zostać w szpitalu jeszcze przez około dwa tygodnie | w podanych zdaniach ukryły sie rzeczowniki w nazwie ˛o' | Śpiewam piosenki | śpiewanie piosenki jeszcze raz (...24 more)<br />
<h3>frpl - pl - phrase-nomatch (last 24h)</h3>
65: slownik polsko francuski<br />
62: polsko francuski<br />
18: ça été ta journée<br />
14: Ramka na zdjęcia | Spędzać czas z rodziną<br />
13: Mam kanał który nauczył mnie wiele | Na oonii<br />
12: Być odmiana | Na łonie przyrody | Ona Na wakacje jeździ do mamy | Spędzać czas z przyjaciółmi | Uczunie sie<br />
11: Jak się nazywa twój | Moja rodzina składa się z czterech osób | Na rynku | vidange a prevoir<br />
10: Justyna mówi po angielsku i portugalsku<br />
9: Lustro wisi obok drzwi | Piosenki Joe dassina | Tak to prawda | Wy jesteście super | Zmywać podłogę | pazdziernik po francusku<br />
8: Bullet Jurnal | Kuchnia przenośna elektryczna<br />
7:  (...4 more)<br />
<h3>frpl - unknown - phrase-nomatch (last 1h)</h3>
9: A la toute vitesse<br />
8: Meurs de faun | Pay Bas | Pay bas | Pies przewodnik<br />
7: L'apport nouveau | Peste porcine | la carte<br />
6: Emploi de temps<br />
4: A la toute vitrsse | Continuer jusqu’a | Les principaux | Mouth ulcer<br />
3: Cho cho | Ssij Penis | Współczesna francja<br />
2: Celles liée | Contre coeur | Faire le proposition | Joyeuse fête, je vous souhaite beaucoup de bonheur d’amour et de santé. | une chose du moins<br />
1: chambre garçonnière | très dair | ty musiałaś zostać w szpitalu jeszcze przez około dwa tygodnie | voix off (...86 more)<br />
<h3>frpl - unknown - phrase-nomatch (last 24h)</h3>
15: Contre coeur<br />
13: En parallele | Faire appeler<br />
12: Maillot de baon | Sclérose en plaques<br />
11: Le foi | Mettre en relation | bienvenue en france<br />
10: Choruję na pęcherz moczowy | Date de 1 ere mise en circulation | En haute couture | Faire le proposition | Filet de peche | LA belle vitrine | Mój pokój jest na pierwszym piętrze | Ça va super et toi ?<br />
9: A la toute vitesse | Au conditionnel | Celles liée | II y a des nuages | Na obrazku | Oni świecą | Sclérose en plaque | passer l’aspiratueur | siege social (...6 more)<br />
<h3>frpl - fr - entry-ids (last 1h)</h3>
33: Efrpl21937107: fondre<br />
32: Efrpl21893389: bas-fond | Efrpl21936974: fond | Efrpl34894080: dans le fond<br />
19: Efrpl21993002: savoir-faire | Efrpl53844740: passer/donner un coup de fil<br />
18: Efrpl21954195: jamais | Efrpl31443728: mettre la main à la pâte<br />
15: Efrpl21963327: mettre | Efrpl33323162: mettre en question | Efrpl37015884: mettre<br />
14: Efrpl21956301: laisser-faire, laisser-faire<br />
12: Efrpl21922537: donner | Efrpl21932812: faire-part | Efrpl21993008: savoir-vivre, savoir-vivre | Efrpl31458976: faire des vagues<br />
11: Efrpl21914428: cultivé | Efrpl21914436: cultiver | Efrpl21922522: donné | Efrpl21932612: faire | Efrpl21983363: qui est-ce que | Efrpl37018764: Faire fi<br />
10: Efrpl21910416: contrecoup | Efrpl21920485: devoir | Efrpl21983371: qui est-ce qui (...1 more)<br />
<h3>frpl - fr - entry-ids (last 24h)</h3>
111: Efrpl21993002: savoir-faire<br />
109: Efrpl53844740: passer/donner un coup de fil<br />
98: Efrpl21976365: peut-être<br />
94: Efrpl22012401: voir<br />
85: Efrpl21973723: partir<br />
69: Efrpl22012994: vouloir<br />
67: Efrpl36972145: avoir un coup de coeur<br />
61: Efrpl33392193: avoir l'esprit mal tourné<br />
55: Efrpl21912407: courir<br />
51: Efrpl21913676: croire<br />
31: Efrpl21997164: sortir<br />
29: Efrpl21912272: cour<br />
24: Efrpl22012513: voiture-lit, voiture-lit<br />
22: Efrpl34092084: répondre<br />
21: Efrpl53908338: taille-haie<br />
20: Efrpl21914877: dans | Efrpl21986489: regarder | Efrpl22012507: voiture-bar<br />
18: Efrpl21949516: impliquer<br />
17: Efrpl21901560: casser | Efrpl22012498: voiture<br />
16: Efrpl21891676: aveuglement | Efrpl21891682: aveuglément<br />
15: Efrpl21888038: arbre | Efrpl21937569: formidable<br />
14:  (...2 more)<br />
<h3>frpl - pl - entry-ids (last 1h)</h3>
16: Efrpl22073767: kiedykolwiek<br />
14: Efrpl22101081: odbierać<br />
12: Efrpl22097564: nieważny | Efrpl22149424: ważny<br />
10: Efrpl22054874: dziennikarz | Efrpl22145067: tylko | Efrpl22164506: zbierać<br />
9: Efrpl22104159: oliwka<br />
8: Efrpl22096993: niespokojny | Efrpl22119991: prysznic | Efrpl22121729: przeprawa | Efrpl22151629: winogrono | Efrpl22158864: zabierać<br />
7: Efrpl22070232: jeden | Efrpl22085430: łosoś | Efrpl22113920: podziw | Efrpl22130496: sardynka | Efrpl22143661: tort | Efrpl22153348: wrzask | Efrpl22160814: założyciel<br />
6: Efrpl22067903: importer | Efrpl22141898: tak | Efrpl22160077: zajmować | Efrpl22164333: zażarty<br />
5: Efrpl22058975: finał (...15 more)<br />
<h3>frpl - pl - entry-ids (last 24h)</h3>
51: Efrpl22143276: tłumacz<br />
29: Efrpl22118523: praca<br />
28: Efrpl22156104: wymowa<br />
24: Efrpl22071058: język<br />
23: Efrpl22047259: cześć | Efrpl22047304: część<br />
21: Efrpl22133614: słyszeć<br />
20: Efrpl22061602: gdzie<br />
19: Efrpl22084384: lubić<br />
18: Efrpl22122684: przez<br />
17: Efrpl22073767: kiedykolwiek | Efrpl22084372: lub<br />
16: Efrpl22060151: francuski | Efrpl22133403: słownik | Efrpl22142025: tam<br />
15: Efrpl22087827: mądry | Efrpl22121729: przeprawa | Efrpl22132248: skąpy | Efrpl22145638: uczyć<br />
14: Efrpl22106024: ostatnio | Efrpl22107454: PAN | Efrpl22107460: pan | Efrpl22142163: tapeta | Efrpl22170607: życie | Efrpl31694926: pozdrawiam!<br />
13:  (...5 more)<br />
<h3>frpl - fr - translation-ids (last 1h)</h3>
7: Tfrpl21953941: issue de secours | Tfrpl21979075: porte de secours | Tfrpl21993782: sortie de secours | Tfrpl21997134: faire en sorte que | Tfrpl22013491: warning<br />
6: Tfrpl21886714: bon anniversaire! | Tfrpl21955082: joyeux anniversaire!<br />
5: Tfrpl21886689: bonne année! | Tfrpl21904938: comme ci comme ça | Tfrpl21907469: comme ci comme ça | Tfrpl21921116: dire | Tfrpl21931302: excuse-moi/excusez-moi! | Tfrpl21931303: excuse-moi/excusez-moi! | Tfrpl21985447: réciter | Tfrpl22007323: qu‘est-ce que c‘est ce truc là bas?<br />
4: Tfrpl21884766: ajouter qc à qc | Tfrpl21929302: sans espoir | Tfrpl21962961: merci à vous pour tout | Tfrpl21987232: remettre du sel dans les légumes | Tfrpl21988050: je te repasse maman | Tfrpl21989817: au revoir | Tfrpl21995602: rien de plus simple à réaliser! | Tfrpl22004630: tour de France<br />
3: Tfrpl21897340: on a bu une bonne bouteille de vin | Tfrpl21907510: comment ça va? (...41 more)<br />
<h3>frpl - fr - translation-ids (last 24h)</h3>
73: Tfrpl21907469: comme ci comme ça<br />
42: Tfrpl21935457: fin de siècle<br />
38: Tfrpl21890747: bon appétit! - merci, vous aussi!<br />
29: Tfrpl21907512: comment est-ce que ça s'appelle en français?<br />
28: Tfrpl21962960: merci bien<br />
27: Tfrpl21907510: comment ça va? | Tfrpl21995210: si | Tfrpl22007303: si ça se trouve, il va pleuvoir<br />
24: Tfrpl113748063: la persistance de taux d'intérêt élevés<br />
23: Tfrpl21962961: merci à vous pour tout<br />
22: Tfrpl21982727: pute<br />
21: Tfrpl21996472: du soir au matin<br />
20: Tfrpl21891835: il n'y a pas de quoi!<br />
19: Tfrpl21962959: merci | Tfrpl21973413: parler français<br />
18: Tfrpl21899278: ça va? | Tfrpl21996316: et ta sœur[, elle bat le beurre]?<br />
17: Tfrpl21973102: mille pardon(s)! | Tfrpl21986685: tous mes regrets<br />
14: Tfrpl21973174: un des deux parents | Tfrpl21997134: faire en sorte que<br />
13: Tfrpl21891827: il n'y a pas que l'argent dans la vie | Tfrpl21973689: cours particuliers | Tfrpl21985288: pantalon/chaussures de rechange<br />
12: Tfrpl21902956: bonne chance! (...5 more)<br />
<h3>frpl - pl - translation-ids (last 1h)</h3>
8: Tfrpl22149264: obraz nie jest wart swojej ceny<br />
7: Tfrpl22121724: przepraszam, która [jest] godzina? | Tfrpl22141347: światła awaryjne<br />
6: Tfrpl22044271: trzoda chlewna | Tfrpl22070007: jasno | Tfrpl22137756: sypki | Tfrpl22156816: wyraźnie<br />
5: Tfrpl22042682: będę zawsze o tobie myśleć myślał | Tfrpl22046137: co tam? | Tfrpl22071099: językoznawca | Tfrpl22081210: gdzie kucharek sześć, tam nie ma co jeść | Tfrpl22099404: dziękuję, jestem po obiedzie | Tfrpl22121722: przepraszam Pana! | Tfrpl22121723: przepraszam cię! | Tfrpl22140453: śledzić aktualne wydarzenia | Tfrpl22142038: co tam! | Tfrpl22154077: wszystkiego najlepszego!<br />
4: Tfrpl22039866: w bliskiej przyszłości | Tfrpl22048169: w dalekiej przyszłości | Tfrpl22080456: nie wiem, co się za tym kryje | Tfrpl22102733: odtąd będę wstawał wcześniej | Tfrpl22113961: poezje | Tfrpl22124082: w niedalekiej przyszłości | Tfrpl22124083: w przyszłości | Tfrpl22150796: do widzenia!<br />
3:  (...39 more)<br />
<h3>frpl - pl - translation-ids (last 24h)</h3>
53: Tfrpl22149264: obraz nie jest wart swojej ceny<br />
43: Tfrpl22141906: kocham cię – ach tak?<br />
32: Tfrpl22116394: w porządku!<br />
28: Tfrpl22069323: w istocie<br />
27: Tfrpl22165344: jak zdrowie?<br />
26: Tfrpl22094251: następny proszę!<br />
25: Tfrpl22055145: dziękuję [bardzo]!<br />
23: Tfrpl22094772: dziękuję, nawzajem! | Tfrpl22129351: proszę się nie ruszać | Tfrpl22144993: mam cię!<br />
20: Tfrpl22043064: cała ona! | Tfrpl22043065: cała nuta<br />
19: Tfrpl22117316: to nie potrwa długo<br />
18: Tfrpl22043026: w całości<br />
17: Tfrpl22069660: jak się masz?<br />
16: Tfrpl22094463: nie lubię ciastek, natomiast uwielbiam lody<br />
15: Tfrpl22032018: ach, jakie to dobre! | Tfrpl22033373: śpiewać altem | Tfrpl22044115: mieć dobre/złe chęci | Tfrpl22130211: w rzeczy samej | Tfrpl22165231: zdobyć się na zrobienie czegoś<br />
14: Tfrpl22130351: mieć dobre/paskudne samopoczucie | Tfrpl22130436: sandał | Tfrpl22153211: wywrzeć na kimś dobre/złe wrażenie<br />
13: Tfrpl22130214: sama sobie zaprzeczasz (...1 more)<br />
</body>
</html>
"""

keyword_list = text.split("<h3>")
nomatch_list = []

for element in keyword_list:
    if element.find("keyword-nomatch") != -1:
        nomatch_list.append(element)

nomatch_keywords = "".join(nomatch_list)

# Replacing phrases and special characters that are not dictionary keywords
# Storing text with nomatch keywords in no_special_characters

no_special_characters = (
    nomatch_keywords.replace("<br />", "|")
    .replace(":", "|")
    .replace("...", "")
    .replace("(", "")
    .replace(")", "")
    .replace(" more", "")
    .replace(" ", "")
    .replace("\n", "")
)

# Removing digits from the text and storing the rest in no_digit
no_digit = "".join([i for i in no_special_characters if not i.isdigit()])

# changing no_digit text into list by spliting the keywords using |
list_of_nomatch_keywords = no_digit.replace("||", "|").split("|")

# removing duplicates
list_of_nomatch_keywords = list(set(list_of_nomatch_keywords))

# Removing empty elements, special characters from the list_of_nomatch_keywords

unwanted_keywords = []
for element in list_of_nomatch_keywords:
    if (
        element == ""
        or len(element) > 50
        or "#" in element
        or "$" in element
        or "&" in element
        or "%" in element
        or "frpl" in element
    ):
        unwanted_keywords.append(element)

for unwanted_keyword in unwanted_keywords:
    list_of_nomatch_keywords.remove(unwanted_keyword)

print("Number of keywords to be checked in dictionary: ", len(list_of_nomatch_keywords))
print("List of keywords: ", list_of_nomatch_keywords)

# SELENIUM PART

# disable cookies:
ops = options()
ops.set_preference("network.cookie.cookieBehavior", 2)
browser = webdriver.Firefox(options=ops)
# loading the pons website
try:
    browser.get("https://pl.pons.com/t%C5%82umaczenie?q=&l=frpl&in=&lf=fr&qnac=")
except Exception as exc:
    print("There was a problem: %s" % (exc))
# keywords input
input_elem = browser.find_element_by_name("q")
input_elem.clear()
input_elem.send_keys("test")
input_elem.send_keys(Keys.RETURN)

final_list = []

for keyword in list_of_nomatch_keywords:

    time.sleep(3)

    input_elem2 = browser.find_element_by_name("q")
    input_elem2.clear()

    input_elem2.send_keys(keyword)
    input_elem2.send_keys(Keys.RETURN)

    time.sleep(3)

    if "fuzzysearch" in browser.page_source:
        final_list.append(keyword)
    elif "no-dict-results" in browser.page_source:
        final_list.append(keyword)

browser.quit()

print("Number of keywords BEFORE checking: ", len(list_of_nomatch_keywords))
print("Number of keywords AFTER checking: ", len(final_list))

print(final_list)