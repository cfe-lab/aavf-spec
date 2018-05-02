# Formal AAVF syntax

```EBNF
<aavf>          ::= <header><column names><record>+
<header>        ::= <header field>+
<header field>  ::= '##'<string>'='(<params>|<string>)
<column names>  ::= '#'(<string>'\t')+<string>
<params>        ::= '<'(<param item>',')+<param item>'>'
<param item>    ::= <string>'='<string>
<record>        ::= (<string>'\t')<string>
```
