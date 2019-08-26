import tkinter as tk

from gs import gs
import unittest


class GSTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_enter(self):
        app = gs.GS()
        app.focus_set()
        app.after(500, lambda: app.destroy())
        app.after(300, lambda: self.assertTrue(app.winfo_ismapped()))
        app.mainloop()
        
        with self.assertRaises(tk.TclError):
            app.winfo_ismapped()


if __name__ == "__main__":
    unittest.main()
