localcrawl
==========

.. image:: https://travis-ci.org/svenkreiss/localcrawl.svg?branch=master
    :target: https://travis-ci.org/svenkreiss/localcrawl

Run ``localcrawl --help``:

.. image:: https://raw.githubusercontent.com/svenkreiss/localcrawl/master/docs/help.png
    :width: 450

You will need PhantomJS. On a Mac:

.. code-block:: sh

    brew install PhantomJS

PhantomJS is pre-installed on TravisCI.


Example Run Command
-------------------

.. code-block:: sh

    localcrawl --start _build/html/index.html --out _crawled/ --depth 3


Mustache Example
----------------

This can be used to convert templated files to HTML files (e.g. for validation
with `html5validator <https://github.com/svenkreiss/html5validator>`_).

Input:

.. code-block:: html

    <html>
    <head>
      <title>Mustache Test</title>
    </head>
    <body>
      <div id="output"></div>

      <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mustache.js/2.2.1/mustache.min.js"></script>
      <script>
        var data = {
          item: 'Fork',
          price: function() { return (1.10 * 1.08).toFixed(2); },
        };
        var html = Mustache.render('{{item}}: <b>${{price}}</b>', data);
        document.getElementById('output').innerHTML = html;
      </script>
    </body>
    </html>

The crawled output includes the output from processing the template
(``Fork: <b>$1.19</b>``):

.. code-block:: html

    <html><head>
      <title>Mustache Test</title>
    </head>
    <body>
      <div id="output">Fork: <b>$1.19</b></div>

      <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mustache.js/2.2.1/mustache.min.js"></script>
      <script>
        var data = {
          item: 'Fork',
          price: function() { return (1.10 * 1.08).toFixed(2); },
        };
        var html = Mustache.render('{{item}}: <b>${{price}}</b>', data);
        document.getElementById('output').innerHTML = html;
      </script>


    </body></html>


Should play nice with:
----------------------

JavaScript template engines / JS frameworks:

* `Mustache <https://mustache.github.io/>`_
* `Handlebars <http://handlebarsjs.com/>`_
* `React <https://facebook.github.io/react/>`_
* `Angular <https://angularjs.org/>`_
* `Ember <http://emberjs.com/>`_
* `Embedded JS <http://www.embeddedjs.com/>`_
* `Jade <http://jade-lang.com/>`_


Static site generators:

* `Jekyll <http://jekyllrb.com/>`_
* `GitBook <https://www.gitbook.com/>`_
* `Octopress <http://octopress.org/>`_
* `Pelican <http://blog.getpelican.com/>`_
* `Middleman <http://middlemanapp.com/>`_
* `Hugo <http://gohugo.io/>`_
