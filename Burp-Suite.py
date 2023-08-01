################################## BURP SUITE ##################################

Burp Suite is a collection of different different tools or framework or de facto tool.

Burp Suite, a framework of web application pentesting tools.

Burp Suite (Embbedd browser) is a proxy server(intercept request & response) or burp proxy (Man In The Middle).

Note : community edition web application scanner are not present (automatically find vulnerability).


There are different types of components :
    
    ● Proxy (Intercept) - What allows us to funnel traffic through Burp Suite for further analysis (like data, packets , headers).

    ● Target - How we set the scope of our project. We can also use this to effectively create a site map of the application we are testing.

    ● Intruder - Incredibly powerful tool for everything from field fuzzing to credential stuffing and more(mainly used in brute force).

    ● Repeater - Allows us to repeat requests that have previously been made with or without modification. Often used in a precursor step to
                 fuzzing with the aforementioned intruder.

    ● Sequencer - Analyzes the 'randomness' present in parts of the web app which are intended to be unpredictable. This is commonly used for
                  testing session cookies.

    ● Decoder - As the name suggests, Decoder is a tool that allows us to perform various transform on pieces of data. These transforms vary
                from decoding / encoding to various basesor URL encoding.

    ● Comparer - Comparer as you might have guessed is a tool we can use to compare different responses or other pieces of data such as site
                 maps or proxy histories (awesome for access control issue testing). This is very similar to the linux tool diff.

    ● Extender - Similar to adding mods to game like Minecraft, Extender allows us to add components such as tool integrations, additional
                 scan definitions, and more!

    ● Scanner - Automated web vulnerability scanner that can highlight areas of the application for further manual investigation or possible
                exploitation another section of Burp.

                
    

