localcrawl
==========

Crawl rendered JavaScript templates from a local server.

You will need PhantomJS:

.. code-block:: sh

    brew install PhantomJS

Example:

.. code-block:: sh

    localcrawl --start _build/html/index.html --out _crawled/ --depth 3


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
