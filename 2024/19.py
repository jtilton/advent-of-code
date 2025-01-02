from runner import Runner
import sys

from runner import Runner
import sys

real_input = """
bwwww, gwwug, ruw, wrbuwrbw, ugugb, rwwgw, wwb, ubgg, rubbwu, wgbuurbb, wrrbru, gwg, uuwwg, ugrrgr, uugrb, grwb, gwrb, buwrwuw, wrb, ruuggwr, rub, guwwr, gwrur, uug, ugguwru, uwr, rwuug, bwgw, ruu, wrbb, wub, wuwgugg, grgwrww, bgubw, wruuuu, bwg, wu, wbrbgr, bgwg, bgrubu, ggru, bgguww, rubgugrw, grwguu, wbg, ugub, urbwuurr, grb, ug, gbu, gbgwurbw, rrrburr, uggru, rubuwrrw, guwgrb, rbr, uruw, gggur, ugwg, bbwrr, ggbbbru, grbug, uuubww, rruug, ubbgwgr, brb, rbbuwbu, ggbrru, uuwugb, ubbgr, bubg, grbb, rgb, rwur, ubuuu, gwuwb, bubgrgr, wuuu, bwwg, urugg, wubuwubw, wgrb, gwggrgu, rwbu, bbbubgrg, rw, ggug, gwbgwbrb, bgugww, ggurrwg, rbbwuwu, wgw, bwb, bbw, urru, ugg, uwguu, wggw, wgr, urrr, urguwr, bbb, bgwbgub, guw, gu, gurwr, rgw, wbb, wggu, brbbg, wbw, rur, gub, rrbbr, uugruww, rbbrb, bwgrgr, rwrurww, grurg, brur, wbr, rgu, gguwr, bwurb, grguw, wuu, rwu, ubu, wbbwwub, urg, rww, bgg, wrwg, ugr, uru, urwggw, buwur, bbrgbwgr, bggbbgw, bbgu, rurrr, ugww, uurbur, brbw, wgwrbr, wbuuw, gwgu, rbw, gbwugwb, gbw, bwwgwr, wurrgwu, wwbg, rburuu, wrruwg, gg, bbbwugg, g, bg, wwguuu, gruwgu, ggrr, ur, bwwru, rwgub, rgwuu, wur, wuwrugw, uw, bubggbr, ubug, gwbbrw, rubgwg, rwbuub, rgrbugb, rbgb, wwgb, brbgw, uwwr, rbrg, uwrrur, uuwb, wug, bwwgrgb, rg, wuwww, bgrb, uurgw, rrburg, wubg, rwrwur, rwb, wrw, bwrw, wg, wwgrubwg, bugb, uuubguuw, gruu, wggruuu, urwu, wuugb, rrwww, bwrugbrb, wrgg, bru, ggww, wrbrrg, ugbu, rwwrrguu, wrg, buguu, ugbbww, urwur, grr, uuw, rrub, rb, bww, wgwr, ubb, bbbuub, ggbrw, rbwb, ubw, uuwg, wgrrbr, grw, gwu, wuwwgr, rwuw, gbbr, bguur, gwgrrw, bbu, ggg, grg, urbwwrr, bwgbuw, bw, gbrw, wbwrb, rurg, uurg, guugb, uww, brrbggbu, ruww, ru, rwguw, wgwbug, wwu, wgwwbur, bu, rguu, uwwwg, rug, wwg, brg, uwu, ubr, burg, ruug, rwr, uurugu, gr, uwubu, rr, rbwrbw, gw, uwwuu, ruuwb, rbg, wwrw, wruubg, bgwgrwbr, wuru, ggrgr, br, rwuu, grgbgg, urw, uub, rgrbb, wbuwb, wgwbg, ubwu, gwb, uu, rrrr, rru, gwr, uuubu, grgw, gbb, gwug, wbggwu, gggr, wr, wuw, wgg, buw, gbuwrwu, gb, uwb, bgubgb, rggbbbu, rgubgggr, rbgr, ruwr, wwr, grgbrb, ugrubr, ubgu, ugw, ugrr, ubg, ubgb, urb, wgb, wbwrbw, rugrr, ub, gbr, bugrg, ugu, rgrw, rrrrurr, bgbw, wgwg, guu, wrrubu, www, wrbu, bgrguwr, wwur, ubgbgug, wbwu, buu, gbgubrw, b, ggr, rrg, wwwb, wgrrrw, ubgrug, rrr, ugbb, wugubbur, bgwb, buwww, ugb, buub, wbrru, wuwguur, gwrggg, bgb, gru, bwwr, bgr, gbbw, wuruw, gbrgu, uwg, ubrg, ggu, bbwg, ugrbug, bbr, r, ugbwub, ggb, bbg, bggwb, bub, gbg, burbr, brw, wbuu, gugbb, uwubg, gbgwr, bgwwru, rgugb, uubgr, bb, gug, rggb, wugub, wrgu, wrwguug, gur, wru, bgbr, bug, bwu, ubbur, uurugb, ubgug, bgrr, bgbb, uwbrrug, bburur, rgr, brbbrw, rrrrwu, rgg, urwuwr, wwgr, bur, rugwg, bgu, urbg, wwrgbuw, rrgwrbb, uuu, grwgg, bwr, wrbrb, wrr, uwuuur, rrubu, ugwrg, rwuwg, wgu, rwru, rrww, urr, rwg, bgw, rbb, bgbubrg, bwbb, u, wggurggu, bubgw, ggw, gugg, ugrru, wbu, rggrrb, ubrgggwg, bwuu, rurb, wgrrg, brr, rubr

wbugbugbgrgwubgrrgrubgbwubugrbrrubgwggggubrrrwrbr
wbgrbrgbwrrurrrguwbubburbrwgwrbuwrbwgwuwubwurggbrggbr
urbrbuwgbgwwwbgbwrugruburguwgwbgrugwrrbwbubgrwgww
rrbgwgrwbrbuubbuugrurgbrbrwrbrggurwgwrbuwuwgubuwwrru
uburbwruugurrbwbgbggrgrrurrugwuwggggubuwugbgurgugurbbbu
wbubwwubrurggrrbbbuuwuwgggbguubwuubbwggrgubwbuggrbrrubg
bbwbgggrwrrbwurubbrgugrguwrwwrrguurwwburgruwrrbrrbwgbggw
gugrgwgbbwguuwbbrgwrruuuruwgbrurwubggbubbgrugubgbuwwgww
bbrbbwgwwwbrgbrrgwgugwbwwrrbbwwgrwrrrrwwgrbguububgwrgww
ubuuuwrrwgwwgbguuurrgwrbbuggruurbwuwrubuugrwuuuwbwgubbuwgww
uwuuwwwrrruggbbggrgwbbggwgurruwwgrugwrgww
ubbbrbbgubugugggugrbwuwbgbbruguburwugrubug
rwwruggrwguwguwgguruubrggbgbbubwwrbbgbwbwwbbubbruwb
brubrbrurrbugwgrgrruuurrbgguwuwubbggbwgurbbuwugur
wwrguwbwuggubgbrgbguburugbbwugrwwwggwwgbrgwrugrwuubgwwrggw
uuugwubwgwrbuurbrwuuuubwgbubwbwrgbgrrbbggrwbwbg
brgbbrugbwbbwbuugubwrbuggruubrgwwuggugbubbgub
urbrwguurgbbrgbwrugggwwgwubbguwrurbwburrwgu
uwrbgggguruwubgrruwrguuuubwugwwrgbgubwrwguubuubwugwbw
guugwbgwbrgurbrbwwrrubbbuurruuubburgrruwguwwwww
wuugwbwbrgbgubgwuwwbggbubrugubrgggwgrrbrrrbuwgbb
wgwgwurrrbwbwuuwgbwrggwruuuwbuuuuwrrbrrbbugwuubrwu
wrbbgbbgugbbwwurruuruguuwuwbubbgruwurwruggruwbrbbwbwwbu
gwbgwbbwwwuubrubguggguwbguuwrubwbrgwwugwbuuwurwrgurub
ugubrbubwbruubwugugrrbwbuggbgbrrgbrrgbbbgrguwwbrgww
ugbbburwwwbrrbrwbrwwbrwwubrrrwwubwgrrrbbgrwbbub
uuuwgbgbuwguururugrbbbwuwurbuubuggbururrgbwuwwrwuuguuugwgww
rwrbrgbuggwwbggwggrrwbgggwggurrbwbbubrgbuggbbrrugrbwwuwrrgww
brggrbgbruwrggwbbbuwubuwgwbrwgrwrwrwruuwggwrruwgrbru
buwugrgrbggwrbuggbubwwugugggbbrggwugbugburgrrbgbuwr
urrwwwgwrbgwgbuwrggggrgbburwgwuuguwbwrrbbwwbgbwrwwwwwgrgww
uwwbgwbbbggwbbbrgubrrrgbwwrwwbwbuwurubgww
bbrrurwwggrbgwggrrggrrgugbubwuwbbwrbrgubgggbgu
wbuugbubuwbrugrwgwbrrgggrubrbrwbgrgwgbrwubgrgww
ggugbrggrrbrgbbwguuruwurggbbggrbugbgwrbwbugbwwuurwgbbggwub
urbwbubwurrgrruubwurbwwrwuwguurrrgbwgbwguwrgbgwwrwrugbbw
bbrgwuubwrgubbrrgrwgugbrbuwuwuuurwgwgbgrbubbbruuubgwg
wwbwbbbwurgubggugrbwrrbwuugugwbrrwuwbrwbrrrbrwbbbgrrrwgwgww
uwwubwgubbwwugrugbwrugwbrwrrwbbgbugruwbwggruguubbrw
uuruwbgwbwbrggrbgrugbgwwbbbgugurgrgggurbwrrwurguu
brbgrruwguugwbuwubwwbgwgbugbgrubrbbubbwubbuggbrgbrwugbrwwgww
brwrbwugubuguuuggrurbwruugguwugwgugwrbrbgwwrbwuurwwuur
bbbguugubrugurrrgugggwbrrrgrggbugwwurrgrwuguwgbwrbgwgwg
burrrgruugbbugrwgbrwrrgrugwrwrgbrrbgwwbbuubgw
gurrgwuubbruwuwgbugbbbrwuwgbwurrurrugurruugrgbbrb
buwurgurguguuuurbrrwgwgbgbwubrgrrrgbrbuwggwrurbggurb
wbgwgbgrgbwubwgubbbbrggrwwgwuuubbbrbwburgww
bgrugwbgbwwwrugrgbbwwrrgurrbwurwurggwbwbbwbruu
wbrwggwrwbggwwurwbububbuwbwwuwwurgggwugbbuwgurruwg
ububrrrruwrwburrggbgwwbururuwuurugrbrrrwrbgbb
gbgrwggrguwurugrrrbbbubwrugrwubuwurwuguggwwrbr
wgbguuwbbrrrgruwgugrgrwgrrugbrgrubugubggbrbwwrwwwwguwugu
rwuurububuubburbwwbbuubbrgrrbubbwgbwrrguwrrbubrgggwgww
rrrburbguwrrgrrbgrggggrbwgrbgrwbbbggugbubrw
ggrwgwubbuwrwruwwgwwbbwbgbwggubwgbrrubgww
ugwbbwgubbwurwbbrrbubugbgwwbubbbrgbwgrugrbrrbwgww
grwwwggbwuwrguugrbgrggbubwbbgguwuguurbwgubwuguuwrggwwr
brrwgbuurugrbuwguwuurguwbbwgbwbrwuubruwubwgbgbg
ubrgbwruwguurrburgururuburwwrrguurubuugrbbrbggrwbuuuwrrgww
rbwgguggbrbgbgwgrgrggbgbuwbgububrruwrbrgww
ggrgwuruurgbwururwbbbrbbubgubugwubbbwrurgburg
guuwbwgwurbrugggrwwwbrwrbbggwgugwubbubgggu
wwggrbwgbgbrwwuwbwurgwbubbggbbgwrrggggrbwgugb
burgburgggbgrwbrrrbgwgbwwbubgwwbugubgwgbwwrrwwwrrug
ugbbbrwbgruuwbwwggbwbguubrrrbgbbwbbbgburbgww
uuburguubgubgggwbwggurgguwbbrgbubwuguururrbwrg
gubwuwubrwgugrwwwuwbrgurrwwbrggrbwbggwubgrgruw
guwgrbruruwrbwruuwggrwwwrburgrbggbwugbgww
urwubuwuruubggwwggwuwwggrbrgburwrbruwrbwrrgww
uuruugbuururbguururbgbugguuuuwwgguubwruguwwgww
wgrbguguwgwbguwwbwrrwrwgbubrgurrgwwgwruuggwbwubb
wburburwbgwrwgwwwrwggrwwurrbrrruugurgubrgg
gbguguwwburwgburrgrbgugwgrwrwruwubugbbgugbwggrrrgww
uwgwbruwuurgwgrgbuugbgurwruwrbbugggbbuuwrbg
ubgbwbrrrbwuruurggugwubruwwgurwgbbggwbbwrrwburbb
rgwuuggrurgwwuuuwrruwggrgbwwbuwwbbwurrbggwrwwurrwgww
rbgubuwrwuwrrbbuugwwurruugbuwguwugwrgrgbwburrwub
rurbrrwugbwgwrrbwbwrrubgwrugbwwuggbubwugwrwbuuggbgrrb
grbwwgbrwrurwbwrbgrwrwuwuwburbrwbwugwgwrwgggrbuwb
ugurrgguwbbgbgbgggbrgwbrwwwrbubuurbbwwbgrgww
gubuugurbrrburwgruuuwbbruwuubuggwwwbrwwwbwwrrggwb
ugurrbrgwurgrrwubbgbwwwbgurrruruwrbwgbrbrruuwuwgwwwbgrggbgww
bwurwubwuruwggguwugrrrbwrubbgbuguguwggbwubrwurbwbrwbugwbu
rwubrbbbuuuwuurrbgbugggwbbgbgwurbuuwbruurguggbuuwrrrubwuug
wrgwrrwguggbrwrbuguruwwrbbbwbbwgbwubururubwrwubrw
buwguruwgrwrwwrbgbbrrbggbugwrrugrburubgbggrbbwubwbgguuwubgww
wwubrbrgwrburbruurgurrgrbrwbrbuwugurbwuubwgwrgbuwu
rbwrggwgbrbrrgbrwuwrrrrwurbggwwuwubuugwbugrguubrw
uruggbgubbrrgbrbwwguurggbbugugrrggubuugwwu
ggbrwgbbggbwgwggbbguurgbgbbbubugbbgrugrgubbu
ggbggwbbrgurwrrrgugbgwbgwwwugguguuugrbuwbwbwbrbbgbrbgwur
rbwrbugwrwwwrwwugbbrbrubrrgrugrwrwgbuubuwgwuwgrrrbgww
wgwwrwgwruwgbbbbwgbbgbwgwrwruwwrwwuuurgrwgww
wwgbbuwguuuwbrubbbwrrgbwwrguuggwuubuuwubbruw
gbgbbuwbrwwbrurgwbugbwuwurbugbugwrwgwwbwwuwuwbuuuwr
gbwubuuwurbuwbwuuguguwbwgbgrbgrgburubwbruuub
rwwrgbrrbrbbbrgrwgrgbgwwgrwbbrrguwbwwrgrruugrrgww
wrbgbrgrwuwwgwrbrgwbubwuwwguuuwurgbbrwgwrruwgg
uwrbgrgruwubggrgrguugrgubbwrbwwbubwgugurrbgwrugbgw
bugguuguwbrurrbrggbwwguubrggguuuwgggrbbgrgbrubbrrgrugwwrg
bgwrwbuuwuuwrruwgrrwbuwuuruurgrbgurruwruwr
urrrrbwrrgbuubrbbgggggubuwbbguuwurwgbrbgww
rrbgwubrwbwbuuuguuguubruwrurggwgwgrrgbwbrwurbwbwgrwrgurwwg
wrwurgwrgwgwwuurgrgggguwbgrwuwbwbwrgbbbbguugbbrbrruguwgww
ubwwbugbwwwrrgrbuwbbwuwubbggruuwrbugruwbrbbbubrw
rrbrgggubrbwrrwrwbuubugrwbgwrurbugubwbrubwrbrrbwwbr
ubwbgbgubwgrbgubrbrgurrgrwbgrgrgwrugbwuuwgwuguwwugwgwururg
gwwugugbgwbgggwggwwuubwwurwbbbrggbuuwgbrrggwbwwbbbgru
bgwgbbuuwbrrgrbbuwwwwrwugggrgwrgbubrgbwgrgwgruwuuubgrw
gruurgugwubuwbbbrbgrgwbgrgggrrbuwrbuwbruwwwurbbr
rgrwuwbwbruwwrrwbgwwrubuwrrwrrbbrrugrubbrgbwwurbrwwgww
bggwwrrurwugurgrwwwbrrggrrwgwgwgrbuuubuguw
bbgbuugrgwruwgwubbrbuurbruwwwgwbrugrgurwbgwugwwbrb
urbbggbrurrrrbrbbuuugwgggbggwugggbwwbrgbbrubw
bgguuwrgrwurgbwwubwrggbbggrbrrurwbgwrgguubgurrggrgwbggbg
rgbuwrurggubbugwbubrrgwbbbrubuugubbguwurwguuuugbu
urwuwbbgrgbwggbrbbbbbrggbwwwgrurguwrgubrgwrbwbgwwwgww
bubugwgbwwuwwurrrbububwuwbgbbggwubrbbuwugrwuburgrwgbugwr
brwbubwurgwbggguuwurrbugurrugwrbbbwggbgww
ruguwbrrrbgbwwuuwwbgrwwugrrbuubgrwburwuggubr
rrbugrbrrgwruugrgbrbuggbruguwbwrubbruubrrrgbgrgwgbgbb
bugggurrrrrgbuwbggbwgrgrrbwrgrgrgubuwwurbbwrggrwruwg
rwrggruurbwguuguwbbrwwgrruguuwrrugbbggwgbbuububur
brbggbwwgwbbruubuguguwbruurugwrrgbgbwwgubguwrwuru
wgwurwruruburruwwwgbgbbwuuwbwgurrgwurwbbwrrwwu
ggubruuuubggrgugubugrgguwwgguwwwuruuggubbuwrru
bbbggwrbbgrwuwwbggwrbwbrwrguwgggbwbbrgbuwrrb
wrbbgwgugrggbrwwwbguurwrgbrrwbguuugwrbwubbgwwubrr
bbgbuwurgbgrrwbuurwbgburgwwbbubwggubrburbrbgwrrbwrbuwgug
ruuwrguruburruwwrugbwwrubgrgrruwruurwwwgrgrurr
rbwwwwubwrwrurbrrwuwwbgruuurbwbrwgbrbubgwuubwurgww
ugrbgubuuwwwrbggrrwbbuubwgwbgwrubwgubwubuwubgwuubwruwu
wwwwbbrgbwgrugrgwrgurwwuruubrubgwugwwggrrgg
wbwbwbrwuugburwrgbrbrbwgbwbgwwuruurwbrbgwuuwbr
uubuurwgbrubbbwbgrrrrwuuwgwggwgwwuggggbuurgguuwgw
bbbrbgburggubrgruggggubbbubugbbrgrguurwbugb
urrrwbgrburwuwuguwbrubwgbrgrwgrbrbuwggurgguwrgrugurbwgww
wuggrrwguwwuruugrrbwwgugurburgugurwgrbwbuuwwrubgwgbwuwu
brrrgbrrrwbrwrbgggbbgwgugwruwrwgbbrwwbwrrbgbburgww
wbuuwgbguurgbwuuruwbgbwuuuuwbuggbwwurbwubgwb
uggrrrgwbrgruwrwgugbggwgrwrbubburugbwuuwrwbgugwwbwrguwrwrgww
gbwrrbuguwwwubuuguruurbbwbwbbuugwurwwgbuurbbwugrubrbubbgww
bgrrwruwrwbbwgwuwruwwgbbrwgburbrrrrwwwuwrbgrrbrwuubgww
ubgrgwrgurbgwgwwugbbbrrwgwruuurrwbubwwugurgwggg
grubgrbgwrbbbbbubuwwrwrurrbbrrbububwwwwuuub
rbwrburbgbrbrgwwuwwbgubrrguurwugbugbuggubrwwururrburgurgb
wrwgurbrwgwgwrwugrgugrwbgbguugbbuwrwrrbwggbbgrgwuu
guggwgbgwurbbrrwrwwggrwwgrbubgurgwwwgrgbwwbrwwuwwwrruurr
grwubwrrubwwgwbrgbrwwwgbbbgwurrbbrrgurwwuwwubwbgubuubugrrgww
urgggugwgwurwwbgbbrwbuggwrggbbbbbwuggbrbrruu
rbuuwwwurugubgbgubggbwbwrrrbbbggbgwggggguwwrrrwwr
gbwrubwgwrbwwbguwuwbwbgurgbruwrwbrwwrbrggurwuwb
uggggwrurguggrbgbgrrurubwggrbgrggwrubbwwbbrbwrgwgbuwrbw
ubrwurwuuguuggugrggwwwurgwrgbbubrugbwrrwuguuwruguwbgbr
uruwbwuwbggwgwrwugubrwgbbbbuuggrbbrrwrgww
wbrrrugbruuwgrrwbbwwbrwugwgbbrwrubwuggbwburgwuwwbrubwubwrgww
gbubgrrrbwbgrbgrubrrwugwugubwurwbbrgwrugwgrbrgbrrb
ubrgbuwwwgrgwbuggrrbuwwwgbwbwwrwgugrrrgrwguruggbbbrrugwuuu
rgrbbwbuwrrubgbbgurbbuuuggrgwrrrrbwgwbwurggwruwgbrbggru
grrbuwwuwwruurruuurwguurubwbrrbuwrwguwuwwrwbwbbgbwugbgww
wrubgbugbgbubgguggugbuburwgbggggrwgguuuwwb
rubwbbgrrwwbbgurbguugrwgrwgwrbugbguwbgrgrgrwwgurg
ugrgrurgggbgbgbruwuruwbuubrbggggbbbugrurwgrubwur
grbubbubgwgrggrbggwrbuwbwbuurbrgrwrbubwguwubbwuggr
buwgurrugbbgwwgggbgwrbrwbugrgwgwbwgwuwgrbuwgwurrwwbguruwr
wrrugbgwuwwwubwwgrugbbgwggrgbbwgwwbuuruuuuubguwrgww
urubbbrrwgugrgurgwuurubrbbgbwbrrrrbbwbrrbwrwuugbbbrgww
gwrwbugrbggubrrbgwggugggrwgubuuwrwwbrgrbgrgurbbwurrggrurb
wgbrwwuwwwruuubgrguugrwuwurbrggurbrbgwwbbg
wgbuwubuwwuwwwrbburuwggwgbbwwuuwwrwubrrwubwbbbuu
wurbggguurgwwwrubbrwgubruguugubrrbggwwurbu
ubrrwwuuruwwgbruruuuuwgbgrrgwubbggugbgbwwbu
wubbbwwbubwggburuugruwwuwbrggrubgwrrbuwgww
wrwggrruwugrguuwggbuwwgrwuubbwbwubrgubgggrbwb
rgbbwrbbrwrwgrrrwubwugrgrwwbrwrwuuwubwbgrgrbbbw
bgwbuugbwuwbuuwugrurwrbbgrwbbgurwuuurbuwbwrr
buurguuwgrrwgugwgbwgwgbrwwwurrgrbrrwgbbbgruruurbbw
gurwubgrguurrrggugruurggurggwurwbgrwggwwbgww
rwwbgbggrrgwwwbuwgrbuubrgbbugbuwugrbuwbbwgbbrbuwg
ggrgrbruwrgwwgbgrggwwbuwwuugbwgugguwrrbbbgbgrbuguu
urugrwbuwgbrrrwgrbbwwwubwrrubbbrgwrbwuuwugbur
bbuggbbuwguububruwurwurbgrbuubugbbugwbwrrwrrubw
ubgrbggrbubuwwbguguurgbwguwwbugwgwwbrwbggwguugwbr
ubbbubgrgggbwwwgbbuwbwwwurgrgbrrrbbbubrrbbrwwgbbbgwu
uurrwuubwbbuwrrugbgbwwbgwugubwuugwggwgggwrguggruwggrgbwwwr
brwbwubruurbugubuwbwrggbgbugrgwuubbwbgwbuwggubrwwgub
ugbugrururugrgwubbgwbrwwrwbwggubuuburwurugrgr
uwubgwrgwrugububrgrugbgrgugwwggwbgrurbuuuugubww
bugwwubuwubwgbbrrwrwwuwugwbbbgwrwwgburbbrubw
wburggbbuguwuuwwuuuwbgrggbuggurwbuwuurrwwww
guwwubrbrwrwuubuwuuwrrwuwbgbubbgbgbggbbbgurbwrrurgww
gwwwrgrwwbgrwrbuurgggrubuguguwwbbgrwggwrbgbggbubrwwwwwr
wbubrgwrrgbbbbwurwububuurgbrwggwuwbgugurwwbb
rgrurgugurrrgrrrbgurguuguwburrubgrrbwugbrrubuwbgww
rruwwuugbgwwrruwuwrubwuggwrwrrrwwgwgwuwbbrrr
guwubbguggubuwgwuwbggubrwgwgbwwgwrwgubbwrrggbuggruuruwgww
uggbubwbbrrbrrwrgbwrwbgwguurrrggwwgrggrbgurugb
uwurbwwbrbrwbbuuuuwrgwgwrbgguwbrgwburbugwrrgggbrw
wwbuwwrrrwrgrgbgurggguubburrruuggbrgwbgwbbuuguwbr
gwbwwuwbbrgrbgrwwbugwwbubwwbwuwuwurwuurwubrggggu
wrrwwguugugwwwwgburgwwgbgrruubuwuuwwgrwbur
wrbwbrrwrbbwwrgrugbwbrugrguwuuuwgubwgrgggwwbg
gbbrgrgwurubwwwburbggwwggrgrbgubgwwbuwruwwb
uwgrguuwggggwgwuubbuwrbbwwbwrguubgbuuubwwwwrugrurgbwg
wuugbbbuguuuubguuwwgrrrrwgggbuwrwuruggrwrgu
rgwrbwgwrrgguwgwrguugbgwgrrubrwurwbrgbuggwuwr
rgbuwrrrbwuwggrbuwwruwwurrwuubwguubgrgrrrurrgrruggrr
gbwugrurrbbubuurrurgrggbrbwubruguburguurrwgww
ubgwwwwgwgwguuwbgggrbggwbrgbuwruwwgggwgubrrgwguuwugggwggrgww
brrbrrbrgurwbgubgbruuurgrwbrgbbbrgruwbuwbrrg
gugwuuwbrwwuubugburbuggbrwgrrrwgrrbgrurrug
rggbbwbbubbwgwrbrbwwbrbuuuurwubuguwwgrrwgrrwrurbrwwbrbw
wugrrggurbburuwwrgrgwrgrbbwwuwgubgggggrgww
urbrubuwgwubrwwbggguguwrgrurgbrrgbbuuuuruggrurwgrbubggwgww
wgggwwrbbrrgugwwwburruwrrbuwrwruugggrurrbrrbgururg
grgwggwgubuubwbwbburrwwgbburbgburubwwrbwbrgrw
rbrbubggbbwwwwwbgbbuurbbrgugrgurgbwgwgugurruubbburggbgr
uwuwwbubwbgwrwwubwuugrbwugwgurgbwgbubrrwbbbwbwbbrwgrrrubb
bubuwgggbwurbwrrwguubrbbguggbrugwwbbgrgwgurbuggbbbwu
guguuubwgubbrwbuuugbubggbbbwrrgrrwuuwwbbbwbubbwur
ruwgugwbrbrwuwwgwuwubuwubwwuuwrggrgrruubwwgww
uwgrbwuguwwrgugwgbgbgrwbrrwguubwugbwbubbugbwg
wrwruruwbuwrrbbuuuuggbbgugwrwgbguubguwrwuwbruugwbrggrrbgww
uubwwgwrbgwbwuwgbuwuuwguwrwurwwgwgruuubgrurubguwurbbuwb
bruuburbubrbrgggrrgwuuuburbrrruugbrurwurubgww
ubrwwrrbbgrburbuubgwbbwbgwrubgbwbugbbbrugrrrgbbubugbubgww
ugggwwgbwgbbbwgrrbruwgrrgbgrgrggwubwuwugwgwubggb
ggwrwuububwgugbgrwrwwurwrgwbbbbwwwwubgww
wwggbwgwbuwwwbbwwwwubrurbrgugrgggbbwgwubugbrrrgguguuwb
bwurwugbwgbubgbuugrwbrgbwwuwgburubgwrbguwrrwuubuugwwwwbg
guwbgbwgurgugrrubgrbbbrgwwwbruwgbrwbwuguuubb
wuubbrgggrggbuugrguuwrgrubgggwugruubguuwbgbuwwruruwguggwrw
urbrrwuuuuburwwwgrgurbwwwwbbwwwuwubugwuwggrb
grgrgwwuuwwrwwrwurubburuuwrgwruuwuuwwwrwrrgbgrbwurugrrgrgww
uuwurggbggbuurbburgwwubgwbbgwrbwwuwwgurggguuubwg
uubbbrggwggwrbrbbrwrgwgrbbugwuurbbgrwruwrwguwrwubwbbrrgww
wbwbugbrbbwuburgurwgrbbguwurwwwguwurwbrurbggwgbbrgr
ubwgbgbgrbwburwgrwurwbgbgrgbrwrguwruwgguwwgwbwbgrubg
wruububwggruggbggbwggrrwuuubguuwwwgwwurubrgrwbrgww
brbgruwgwuuuwwgrwguurruwurbubgwgbwbuwugrgrbuuuwwgbwbwgwwr
gggugwbwbggbuurggbwbgbbwrugbrbwrgurbrrubrgwu
grgggbrruwgwurwgwrruwgrrwuurrggrrwugugbwugwurrbu
brubugubruwbwrwguwrurggrbgguurrwrbwwrwrwbrbrugwgurbgguwuww
wgwubuwgwubwubgugwbwurbgwbuwugbbubuguuugugugrubwuggrrgrbgu
wwgbrbggugugwwgrbgbwwrwrrruwuugrbugrrrbggwgwuwwwg
grwbbguugugrgggwrwuwbwwugurbwbgrbwbgubgwgwugrguw
urgrurbbubgrwruwrguugrrwrbrggwwbruwbbwbuuggwrwgugwgww
uwuubrbuugwwbgrgbbgubrbrrgbbguugubrrrgwrbbrg
urgggbuwbbbwgbrguuwrgbwbwbgrwburuwuwguurbgbbur
brbbuuggbwugrgbruuwgrurrbrbugwubwrrwgubgbubgrwbgwrurwurg
bwwgrubwgwgrwuruguubwbwrguwwwggbrubbwubrruggg
uwgrgrrrggurggrrrrgbgbbbgubbbrgrubuwrrwgrrrrrwgrbwwuruggb
gbruuwwubrurugbwrruwbrbbgwgrrgubrrbrurrwbr
wrwbubuwbruwgrwgbugwrburrrrrrwwrgrurugrurwrrbrbgwb
wbgrwgwrgrgwwwrbrrugbwwgggruruwrgwbwrwbubwgbrrbgru
wrbbubgrgwrwwggrwgrbbuuwbwbuggrwurbbrgwwbbbrbgrbguub
gbrurwrrbbgbgugbuwrgubggrurwrwrrrgwgwwwuuuwruuwgww
bbwuwgbrgurwuwbbwrwuwrwbbubrgurwbrrwuwbbwrgwbwbggrgrwu
wggggwbgggwgbwurrgbbwbwrgwuurgurrububgbbbbrgrwruw
rgrugbubugwrwrburrwgrrrrrgwububwrruuuugbgwbwwbbgrr
wgrruwwugwuruwwbrwruruuwgwbbgrgurgubgrgugwuwbwuburrwrbubwu
wuwbbubrgugbgbuggwgurubggrrwrwrwgugurrwrbgubugw
rbbrruuurgwrugwubbrrrbwwrwrbgwgwubuurwgrbgrgrbbruwrgwgb
wwuwrugugbwrgbwgbgbuwrggruuubgurrubuwrurwwgww
brurbgggwrgwurrgwrbggrrbbbwbgbrgbwbuwugwbbgwbwgww
wbgbggguwwbuggubuuwurugubrbwrbwurugbrrubrrbwbbbwgu
wbgwuurwgubrrgrgbuuuwrrrggrggurwurwrrwrggrrbbr
wuwgguuggrgwuwwbgrbwwrbuwrbwbguuwubwggbubgww
guwrwrurgwrgguurrrbugwgurwrbwwubgggbugwgww
grrrbgbugwwggwugbbrrwurwgrrurbuubrbbbwgburgurbwgwwrbgwubgww
ugrrugwbrwbguwbbgrgbugwurgrwbrrbububgrbwgguuwgbuurbb
wgugrruugbgbwbrrwgbgwurbwwgwwwggrguubuwgburugugbbbubuuubrw
grbbbubgrgwuuwruwwuwgugrwugrwbwguuggwguugggwuwubrwbbgubgww
wbubuggwbwguwubbrubrgrwgwugurbuwguuuwbruuuuurbburugw
rugwgrbbgurbuuubgwwwgrgbgggggbwrbwgrwurrrugrwugrubrgbrgww
burbwuguguubrugwrrwurrwbggruuwwuwubgbrgww
urubuugrrbrwwbbrrrbbgrgbgwgrubrgwurbuugwuburrgbubb
bbrgrgugrbgbrrububurwrguwbgrbbbrbgbuuugugbwrubrrg
bbrwrburuwgrugrrwuwbuugwwbgurrwbrgruurbbgwb
wbgwwgubgrrbwbwbbwuwubgbggggububwuuwwururrgrw
rguurbrguwrrbbwurwgubuwgwguwrggwwuubbwrgwrrurwugguw
gbgbrubuugwuuwbwubrgggwgbwwgwbrrguurwuwuubwwuuwuuuwwrwgbuw
uburuurwbrrgurbbwrwuwwwgwgubgbuwuurguwbgwggurbbbbwgww
wurrugwbbrruwrbbrbgguuwubburgburrrrbugbbrrrwbrbrgwuu
rbwbbuwbwrbrwubgrgugbrbrbgubbgbgwwbuuwbbrgrwggbwu
wruuurburwgwwubrwuwrgurrbbrwwwwwbrwwwbbbrggbbubbugbuwbgww
ggugwwwbubbwurgurbugrubggggrrugubrwwggrgrbbgbububbwwwg
rwbbugbggbgrwgbbwrwwbgrwwwrugbuwuubuuuuwurrruwwwwggwrwuuu
wubbuurgrgbwgruubgbugugrwurbrgburubgugrwwrgbubbgww
wuuruuwubwguuugrwwrbrrgbrbwbrwgwubuwrrwubuguurwwrwgww
rgugbwrgubbgrbrbuwwubgrbbrububruwrbbuggbruububrubgugrw
gwuuuwurgbrgwrgguwwgugbbgurrbbbgwrgrggwguwu
wwuubrwwrwrbrugbwrbwuruwbrwrugwbbuuwrrrubuugrrwrwwgww
bgwgurwgwbbbgrwbbwwgbbgwuwuuuwwrgbubwgubbrgrbrwbgrgww
ubggbwrbwbwwbrbbbrwgbgrbrwbbbgwgrrwrrwgww
rwubrubgrrrbgwggwwbrugrubuuwbrrbggbuuurgwggwrbwgwuwugrbrb
buurgguruuwuubggwrrruuwbbuggrbururrbubrbrbgubrwbbgrrgbu
guugubwwbwgugwbrggbbgurgrwwrguwrrurgububbbrbguu
rburuwbbugbubbgurrbguwbgrgwbgwbrbwwgbrrugbugruggrgbu
bgwubburubruubguugbrgwgbbrrgrrurgrwubuubbrurrrw
rugurggbgbgbbbbrwubwgbguwrwgwgwgubwgrggubrrbb
wwwrwbrwuguuubrbbubuguwuugggrrgwggbbrrwbbgww
uugwuwugwuuugrwuwbwrubugbbrwgrrwwugbrwrrurrurwgrwurururgw
rggbgrgrburwurggwwbwwwwugbgbgwwrwgubwbwuwwrgbrw
rrgburrgubrbgubbgbgrurburbwuurrgwuururwgbuwrurruwbururu
bburburrurwbrwwbwggggrgwugrwrbgggburubgrwbgwwwwwuwrrrbb
gwrgrrwwuwbbrubbbwububwbbwwbguuurgwbururwgbgww
urgwrwrgbwuwguuurugwrbgbrgurbuwwwbwgwgrwrbwrguu
gubgbbbrbwbwwrbbgbrrwrbuggugwbuwbuubbubrwwwbbwbgg
rgrwrgrurbuugrrwrrgrrgbbwgwubrgbgbbgugbrubwbw
brbbwwgrrbuwubwrbrwbuwwrrgrrwbbwururgguwuubwrggbruuubbb
urrwrgbrugrbbbwrrggwugbgggbgbrbrggrugwbrruubruwbbb
bbbgwuruggbwrbrbwbrrbgwgwwbbgurguurbrgrrugwuguugwurbuurrg
brwgggguwwrgrgugwgrbwguwrggwuuwbguuubrburuu
gbgrrurbrrubwwrwggrrbbbugggbrwbwbwwubbubruuwgur
rwbrwgbwrurgurwwbburrbuburrbuubrwgwwggww
rgbwwbrbrubrurrguwguuwrbbgruugggbgugggubgbwuwu
uwubbbwuwbgbuubbwubbrrrubwurwgbgwurrrgrwwwugggbgww
ggrwwuurwgwruuuurgugurrwwrgwgubrrgugrbgww
wurbwbgwrwrrwubuuguwurgwgrgwguwwuuggwbuggrbwgww
rgwwgbwurbrrwrwwuugwwbwwwubbbgrugrubwgguwgwbur
rgbgurubuguwburuuuggbburuuurwugbgrbwwuurwwgurggbrrgurrruw
uuurgwububbruwwuwwbggugrwrbrwgggwugwbguggrbbgrrrbr
bggwgwuuurwuwuwgrwwuwrgwwuwrguwggwuwwrwbbugwbrggbrwgww
rbrbbbrrrgwrggbbruwuwurrwurwwwguburwgguwbgwgww
urggwgbubuuubugrbrrubwrbgbbbugwrbguugggrwgwubgwbwg
ugwbgbgurbgwbgrwrrbwrrbgbwbgurrrubwgbuwwbgwu
bgggrgbrwrruwbgbgwbrwggggrrrugbuugubbrwubbwbburbgrur
ggbgwgwuuwurwrrwrwbrwgwrurbrubwbbgrrbgggwgg
bwggugbwwruwbrbwrrwrbwbuwwbuburwwrrbwwuguuugw
rwbuuwuwburbgbuwbwwrbwgwgrgurbwuurrbrrgbbwrruwgrgburbgww
gwuwuurwwrbggguwruguwbbwugrrgurruwbuguwugbrwgrgrgrbbrwrbb
brrgwurbuwrugubwgurbwubburbwggrburrbbwgwbgu
uwgwrrugwwurburbgbrbuubgugrwurrubrwbbbgbbugwbububuwb
wbgurrrurubggrurgbbwrbbbbwwurwuwwggrwwrbbrbbuuwgwbwr
rgrbwgrburwwwurgguwubrgbbuwrwubggwwgwgrbwgwugbwww
wuurgwgrugrurwgurbrgguugubrbwugrwgwbugggbwgbbgwbrrbbbgr
brbuwuurwwgwrgwrwwgburrurgwrurwrrbwgrbbwubbgwrugbrubgww
rrggwwgbwbuubuwuguwugwguwuggwruwugbrgbrgrrgwgww
wwgguggwgbrbrruwbubwgugwggwwwrggrggbubbugbruw
ggubrwuwubgrgwrbbwbbubbuwgwugggggrrgugbbggbgwurbwrwwgww
rwwrwwwwrubwuurwugrwubrbubwuubuuggrgrwuubrgubgbuuwgbugwgg
rwrbburrwrwruubrbbbbwgurwrgggwwuwrbgwgrgrgwwbgww
rrgrbuwururuwbruburburguruggbugurgrrrgbbbugwgbuugurwwu
uuuwgrbuwbrwwurgwrrurwurbbbuggrwruubgbbrubgrurwguuubgr
ubrrgwbrgggbwbuguwubgggurwugugugbbrruwbgbwwrururgggbggwub
gubwugrrgggggbwgrwruwrrgbwwuuwgwgbubrwgrrrgwwwww
rbrwrwruuwwgbgubgwrgwuuwbuurgurggwbbwrguugrbrwrbrgugwrwgww
bgwbrwbwruruwggubuuubububbbbrggubwuwbgugrbrburgwwbwwwww
ruubuwrwuubrbrrruwuuwruwwgggbrugrbrrwgwwgugrgrbuwbg
rwwbbuubwwgguuubbwrgrbwwbrwwbbwwwbgbwbgwwbrrbww
rbwrgwwwgwbbgwbwugrbrwwbgugbwubwbuurggbugguuugwg
rrbbuugggwurwwugubburubbbbuggwwgburgwwubbrgww
gggguwrguuwbwbrwwbbuwurgggggubrgbgbbrgrbrrrbbubgg
ggwubgwuwwgrbggbwgwrwbuguuwbubrrgwubwwbuwuuw
rbugbrwuwwbguuwbwggrwrrrgwurbbbuwgugrubgrurbr
rwbrugguuuruguubggggbuurburwwrwgwwbwrggbgugbwbgrbu
rbrgwubguwuwbubruuwugubrgbwrugbwrgwrruwrrgw
buugurrbuuuwgwwggruuuuwwrbbuugwbgwbrbuuggwwgww
ugubururrwbugrbuuruwgwbwbuubguwwgbwrwgggggwgggub
wugruubwwgrubwguwrgrwbubwbruwwbrgubugbrugurrggwgugbgww
rbwgbuwgwrbugubwrgrbbuurwuurbgwgrwguwgwurwrgbrgwgrbwbrurw
rruuwguuwurwuwggrbwwuurgrgbbruwwuwwrrwbugub
bggbbubuggguwwugggwrgrgggbwwgwrwuburuguwbgrbu
bguwgrrwgbggwguwggwwbwrggbugrubwwurrbrwwbuuwrurrrwrw
burwwrguwrbrurgruwbwuwwuurwbbrruguguwbwbgrbwbuug
wruugrgwbrgubbbbuuuwrgrgburgrgbwgbrugwrwrrrbrurwbg
wrbuuwruguurgwbbrgwubbgwwuwrgbbrgwrbubggbwwgub
rgrbwwurrwgwgwrrubwugwgwbgrggbrbrbbubwwgbbbuguubwu
wwrgbgguwbgbururwwbrwwuwuwuuuurbbgwgggbwbbwubrrrggubwg
rbuwgrbubrruguwuggrbuwuuwruuurruuwrrubgbwgg
ubbrwuubgrugrguguggrubrgurrrggubruuwbgwgrrburwggbwrrbgbwrgww
wwrwrgggurbrwrwbbrbuguwbubgwgruguwgrrgubgggrgwubrgww
grwrwubgwuwwgwwwgbrburrgggbbwrwugwwrgubrbrubbggugurg
ugrgwggbrwrbbgrbrbuwgbgwrgbrgwwbruuguubwrbubrurwruubwwurwgww
rrrrubgwwrwurgbuurrrbrrrbbruwwwwbgurwbugbbrrrbgww
wgbuuugggburbwwggwbgugruggwbgbwugruwuwwwwgrwgbwuwr
bububuubwgrrwrwrgubruwubbuubwrguggwugbgbgwgww
rbgrbbugugwwwwubuugbwrruwbbubwbwwggugrbwgw
rguggbwgbuubwbgbuwgbbrbwwurugbbuwwrwgrwuwgbbwguruwrb
wbugurbbgwrrbuguggugwgwbwgwrburbwrugbrbrrwwbrrgwwgww
bgbrwgbrrggwwwgwrbrbggwurrurbubwrrwgbrwgwugubburbgugbbr
bbwrurbwbwugubwgrbbgbbwwbgrbgbwwbggwbruwbgrubbwrww
uwurbrwwrruwgwrguwuwuubgwrgbbwgruwggrrgwrwwbbrbgbgbguwrbgr
rggrbwrrrbgrbggguwuugbuubruwugbrrugwuuugwubb
uugbwbbgwrbbggurgbbbbgwrrwbruurgwgwgbwuubgguuubrwgww
gbwbbgrwwgugurgrggrbwwbwwrwgbbggwrbgwwgww
wuurbgwgrwbrwwgwwbgbggggrubruuubgbbbruubrwgguurbgww
ubburbgurgguuwbruuurwwgburrrbwuwbgruwuburwbwbwrgbrbgww
wbrbwgubuwubrrbugbuwrbbwrwbwwrrbwuruuwbuwbwrwburrrb
ugguuurburwubugrggburuwuuggwwbbwbrurwuuwbwbbgubw
wrbugwggrbwgrrgbwggubgruwgggwggrrgrwwgrgwugbbuw
rgbubwuugrwuwuwwrwurgrrubgrbbbbruuwgwuubrgr
wwgrwuuwrbrwwbuuuurrruruuuurugrbrwwwrguwrwuggwuwwwburgwbb
gwrrggbbggurwubggrurgwwwububggbguurbwwbgurwgrgww
uwuurbbbuguubwuggrbwrububgwbgrrbrwbbgugrrwbrwrbrrrrwg
guubggrguguwgbwrugurbrugruwrwbgbrwrgwwgurbruguubrbubr
wgwbbrggbbggrbwbguubrgguwgwrbbgrruwbrrbbwgggugrgrgr
wrgbrrrgwwbbrrgrgurrwbrgrggbrrgwbugrugbrwwbuwgww
rbrggrrwgugubrrbrbbgwurbbrgwgubrrwwrwwurrurbwwgbu
"""
test_input = """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""

from functools import cache

# P, _,*T = real_input.split('\n')[1:-1]

# @cache
# def count(t):
#     return t == '' or sum(count(t.removeprefix(p))
#         for p in P.split(', ') if t.startswith(p))

# for cast in bool, int:
#     print(sum(map(cast, map(count, T))))

class Node():
    def __init__(self, ch):
        self.ch = ch
        self.children = {}
        self.terminus = False

patterns = real_input.split('\n')[1].split(', ')
targets = real_input.split('\n')[3:-1]
# targets = ['bwurrg']

@cache
def find_target(target):
    if target == '':
        return 1
    
    pre = [p for p in patterns if target.startswith(p)]
    # print(target, patterns, pre)
    return sum([find_target(target[len(p):]) for p in pre])


count = 0
for t in targets:
    count += find_target(t)
print(count)



# class TodayRunner(Runner):
#     def parse(self, input):
#         self.tree = Node('.')
#         self.towels = input[0].split(', ')
#         self.seen = set(self.towels)
#         self.failed = set()
#         for pattern in self.towels:
#             self.seen.add(pattern)
#             t = self.tree
#             for ch in pattern:
#                 if ch not in t.children:
#                     t.children[ch] = Node(ch)
#                 t = t.children[ch]
#             t.terminus = True

#         self.targets = input[2:]
    
#     def find_pattern(self, target, tree = None):
#         t = tree
#         if not tree:
#             if target in self.seen:
#                 return True
#             if target in self.failed:
#                 return False
#             t = self.tree
      
#         ch = target[0]
#         if ch not in t.children:
#             # impossible
#             if not tree:
#                 self.failed.add(target)
#             return False
        
#         next_t = t.children[ch]

#         if len(target) == 1:
#             return next_t.terminus

#         rest = target[1:]

#         # print(self.seen.difference(self.towels))
#         # print(self.failed)
#         # print(target, next_t.ch, '->', next_t.children.keys())
#         # Start a new pattern
#         if next_t.terminus:
#             if target in self.seen:
#                 return True
#             if self.find_pattern(rest):
#                 self.seen.add(target)
#                 return True
#             else:
#                 self.failed.add(target)
        
#         # Continue current pattern
#         return self.find_pattern(rest, next_t)

#     def part_a(self):
#         possible = 0
#         for t in self.targets:
#         # for t in ['urbrbuwgbgwwwbgbwrugruburguwgwbgrugwrrbwbubgrwgww']:
#             if self.find_pattern(t):
#                 if count(t) == 0:
#                     print(t)
#                 possible += 1
#         return possible


#     def part_b(self):
#         pass




# if __name__ == "__main__":
#     runner = TodayRunner(test_input, real_input)
#     print(runner.run('-v' in sys.argv))


