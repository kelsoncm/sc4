"""
The MIT License (MIT)

Copyright (c) 2015 kelsoncm

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from unittest import TestCase
from python_brfied import instantiate_class, build_chain
from python_brfied import BaseHandler, BaseDirector


class TestBaseHandler(BaseHandler):
    def on_start(self):
        self.started = True

    def handle(self, *args, **kwargs):
        self.ran = True

    def on_stop(self):
        self.stopped = True


class TestBase2Handler(TestBaseHandler): pass


class TestPythonBrfiedInit(TestCase):

    def test_instantiate_class(self):
        self.assertIsInstance(instantiate_class('python_brfied.BaseHandler', None), BaseHandler)

    def test_build_chain(self):
        base_handler = BaseHandler()
        self.assertIsNotNone(base_handler)
        self.assertRaises(NotImplementedError, base_handler.handle)
        self.assertIsNone(base_handler.on_start())
        self.assertIsNone(base_handler.on_stop())

    def test_build_chain2(self):
        self.assertIsNotNone(build_chain([]))
        self.assertEqual(0, len(build_chain([])))

    def test_build_chain3(self):
        links = build_chain([TestBaseHandler, TestBase2Handler])
        self.assertIsNotNone(links)
        self.assertEqual(2, len(links))

    def test_build_chain4(self):
        links = build_chain(['test_chain.TestBaseHandler', 'test_chain.TestBase2Handler'])
        self.assertIsNotNone(links)
        self.assertEqual(2, len(links))

        first = links[0]
        last = links[1]
        self.assertIsNotNone(first)
        self.assertIsNotNone(last)

        self.assertIsInstance(first, TestBaseHandler)
        self.assertIsInstance(last, TestBase2Handler)

        self.assertIsNone(first.on_start())
        self.assertIsNone(first.on_stop())

        self.assertIsNone(first.handle())
        self.assertTrue(first.ran)
        self.assertIsNone(last.handle())
        self.assertTrue(last.ran)

    def test_BaseDirector(self):
        self.assertListEqual(BaseDirector([])._first_loader, [])

        base_director = BaseDirector(['test_chain.TestBaseHandler', 'test_chain.TestBase2Handler'])
        self.assertEqual(2, len(base_director._links))
        self.assertEqual(2, len(base_director._links_names))
        self.assertIsInstance(base_director._first_loader, TestBaseHandler)

        self.assertFalse(hasattr(base_director._first_loader, 'started'))
        self.assertIsNone(base_director.on_start())
        self.assertTrue(base_director._first_loader.started)

        self.assertIsNone(base_director.execute(0))
        self.assertTrue(base_director._first_loader.ran)
        self.assertTrue(base_director._links[1].ran)

        self.assertFalse(hasattr(base_director._first_loader, 'stopped'))
        self.assertIsNone(base_director.on_stop())
        self.assertTrue(base_director._first_loader.stopped)
