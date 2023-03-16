import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.paate = Kassapaate()

    def test_kassan_alustus_on_oikein(self):
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
        self.assertEqual(self.paate.edulliset, 0)
        self.assertEqual(self.paate.maukkaat, 0)
        
    def test_maukas_kateisosto_toimii(self):
        self.assertEqual(self.paate.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.paate.kassassa_rahaa, 100400)
        self.assertEqual(self.paate.maukkaat, 1)
        
    def test_edullinen_kateisosto_toimii(self):
        self.assertEqual(self.paate.syo_edullisesti_kateisella(500), 260)
        self.assertEqual(self.paate.kassassa_rahaa, 100240)
        self.assertEqual(self.paate.edulliset, 1)
        
    def test_maukas_kateisosto_ei_toimi(self):
        self.assertEqual(self.paate.syo_maukkaasti_kateisella(100), 100)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
        self.assertEqual(self.paate.maukkaat, 0)
        
    def test_edullinen_kateisosto_ei_toimi(self):
        self.assertEqual(self.paate.syo_edullisesti_kateisella(100), 100)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
        self.assertEqual(self.paate.edulliset, 0)
        
    def test_edullinen_maksukorttiosto_toimii(self):
        kortti = Maksukortti(500)
        self.assertEqual(self.paate.syo_edullisesti_kortilla(kortti), True)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
        self.assertEqual(self.paate.edulliset, 1)
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.60 euroa")
        
    def test_maukas_maksukorttiosto_toimii(self):
        kortti = Maksukortti(500)
        self.assertEqual(self.paate.syo_maukkaasti_kortilla(kortti), True)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
        self.assertEqual(self.paate.maukkaat, 1)
        self.assertEqual(str(kortti), "Kortilla on rahaa 1.00 euroa")
        
    def test_maukas_maksukorttiosto_ei_toimi_jos_ei_ole_rahaa(self):
        kortti = Maksukortti(100)
        self.assertEqual(self.paate.syo_maukkaasti_kortilla(kortti), False)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
        self.assertEqual(self.paate.edulliset, 0)
        self.assertEqual(str(kortti), "Kortilla on rahaa 1.00 euroa")
    
    def test_edullinen_maksukorttiosto_ei_toimi_jos_ei_ole_rahaa(self):
        kortti = Maksukortti(100)
        self.assertEqual(self.paate.syo_edullisesti_kortilla(kortti), False)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
        self.assertEqual(self.paate.edulliset, 0)
        self.assertEqual(str(kortti), "Kortilla on rahaa 1.00 euroa")
        
    def test_kortille_ladattaessa_saldo_muuttuu(self):
        kortti = Maksukortti(100)
        self.paate.lataa_rahaa_kortille(kortti, 100)
        self.assertEqual(self.paate.kassassa_rahaa, 100100)
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")
        
    def test_negatiivinen_lataus_kortille_ei_toimi(self):
        kortti = Maksukortti(100)
        self.paate.lataa_rahaa_kortille(kortti, -100)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
        self.assertEqual(str(kortti), "Kortilla on rahaa 1.00 euroa")
        