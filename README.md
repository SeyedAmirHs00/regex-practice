# Practice on regex

In this repository we want to solve some tasks and by using ReGex 

Source:  
[learn by example](https://learnbyexample.github.io/py_regular_expressions/Exercise_solutions.html)


## Problems

1. For the given strings, replace all occurrences of removed or reed or received or refused with X.

        >>> s1 = 'creed refuse removed read'  
        >>> s2 = 'refused reed redo received'


2. For the given input list, filter all elements starting with h. Additionally, replace e with X for these filtered elements.

        >>> items = ['handed', 'hand', 'handy', 'unhanded', 'handle', 'hand-2']


3. For the given input string, change only the whole word red to brown.

        >>> words = 'bred red spread credible red.'


4. Replace 42//5 or 42/5 with 8 for the given input.

        >>> ip = 'a+42//5-c pressure*3+42/5-14256'


5. For the given string in camel-case write a Python program to convert a camel-case string to a snake-case string.

        >>> s1 = 'AmirAliHosseinTaghi'
        >>> s2 = 'PythonJavaCpp'
        >>> s3 = 'AsgharAkbarSoghraKobra'


6. For the given string in snake-case write a python program to convert snake-case string to camel-case string.

        >>> s1 = 'amir_ali_hossein_taghi'
        >>> s2 = 'python_java_cpp'
        >>> s3 = 'asghar_akbar_soghra_kobra'


7. For the input list words, filter all elements starting with s and containing e and t in any order.

        >>> words = ['sequoia', 'subtle', 'exhibit', 'a set', 'sets', 'tests', 'site']


8. Modify the given regular expression such that it gives the expected result.

        >>> cast = 'dragon-unicorn--centaur---mage----healer'
        >>> c = '-'

        # wrong output
        >>> re.sub(rf'{c}{3,}', c, cast)
        'dragon-unicorn--centaur---mage----healer'
        # output we want
        # dragon-unicorn--centaur-mage-healer


9. The given input strings contains some text followed by - followed by a number. Replace that number with its log value using math.log().

        >>> s1 = 'first-3.14'
        >>> s2 = 'next-123'


10. Extract all occurrences of < up to the next occurrence of >, provided there is at least one character in between < and >.

        >>> ip = 'a<apple> 1<> b<bye> 2<> c<cat>'


11. For the given list of strings, change the elements into a tuple of original element and the number of times t occurs in that element.

        >>> words = ['sequoia', 'attest', 'tattletale', 'asset']


12. Convert the comma separated strings to corresponding dict objects as shown below.

        >>> row1 = 'name:rohan,maths:75,phy:89,'
        >>> row2 = 'name:rose,maths:88,phy:92,'
    

13. Replace the yyyy-mm-dd format date to mm-dd-yyyy format

        >>> date1 = '2012-03-30'
        >>> date2 = '2020-04-03'


14. Delete from ( to the next occurrence of ) unless they contain parentheses characters in between.

        >>> str1 = 'def factorial()'
        >>> str2 = 'a/b(division) + c%d(#modulo) - (e+(j/k-3)*4)'
        >>> str3 = 'Hi there(greeting). Nice day(a(b)'
    

15. Add [] around words starting with s and containing e and t in any order.

        >>> ip = 'sequoia subtle exhibit asset sets2 tests si_te'


16. Replace all whole words with X that start and end with the same word character (irrespective of case). Single character word should get replaced with X too, as it satisfies the stated condition.

        >>> ip = 'oreo not a _a2_ Roar took 22'


17. Convert the given markdown anchors to corresponding hyperlinks.

        >>> anchor1 = '# <a name="regular-expressions"></a>Regular Expressions'
        >>> anchor2 = '## <a name="subexpression-calls"></a>Subexpression calls'


18. Count the number of whole words that have at least two occurrences of consecutive repeated alphabets. For example, words like stillness and Committee should be counted but not words like root or readable or rotational.

        >>> ip = '''oppressed abandon accommodation bloodless
        ... carelessness committed apparition innkeeper
        ... occasionally afforded embarrassment foolishness
        ... depended successfully succeeded
        ... possession cleanliness suppress'''


19. The given input string has sequences made up of words separated by : or . and such sequences will end when : or . is not followed by a word character. For all such sequences, display only the last word followed by - followed by the first word.*

        >>> ip = 'wow:Good:2_two.five: hi-2 bye kite.777:water.'


20. Convert the comma separated strings to corresponding dict objects as shown below. The keys are name, maths and phy for the three fields in the input strings.

        >>> row1 = 'rohan,75,89'
        >>> row2 = 'rose,88,92'

