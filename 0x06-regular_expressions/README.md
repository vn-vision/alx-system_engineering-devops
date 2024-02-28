# 0x06-Regular_Expressions

Regular expressions (ruby regex for short) help you find specific patterns inside strings, with the intent of extracting data for further processing.

    [0-9] matches any number from 0 to 9
    [a-z] matches any letter from a to z (no caps)
    [^a-z] negated range

There is a nice shorthand syntax for specifying character ranges:

    \w is equivalent to [0-9a-zA-Z_]
    \d is the same as [0-9]
    \s matches white space (tabs, regular space, newline)

There is also the negative form of these:

    \W anything that’s not in [0-9a-zA-Z_]
    \D anything that’s not a number
    \S anything that’s not a space

The dot character . matches everything but new lines.
If you need to use a literal . (dot) then you will have to escape it.

# Modifiers

MODIFIER    DESCRIPTION
    +       1 or more
    *       0 or more
    ?       0 or 1
    {3,5}   between 3 and 5

    ()      capture everythung inside ()

# Look Ahead & Look Behind

Look ahead lets us peek and see if there is a specific match before or after.

NAME        DESCRIPTION
(?=pat)         Positive lookahead
(?<=pat)        Positive lookbehind
(?!pat)         Negative lookahead
(? <! pat)        Negative lookbehind

# Regex Options
You can set some options on your regular expression to make it behave differently.

OPTIONS     DESCRIPTION
    i           ruby regex case insensitive
    m           dot matches newline
    x           ignore whitespace


This information is further explained in RubyGuides, Mastring Ruby Regular Expressions by Jesus Castello.
https://www.rubyguides.com/2015/06/ruby-regex/
