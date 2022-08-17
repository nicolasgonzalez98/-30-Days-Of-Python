import re

def clean_text(sentence):
    regExpr=r'\W'
    matches = re.sub(regExpr, ' ', sentence)
    matches = matches.replace('  ', ' ')
    return matches


sentence = '''
%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. 
There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;
I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

print(clean_text(sentence))