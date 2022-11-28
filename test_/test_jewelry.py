from POM.jewelry import Jewelry
from Data.reading_objects import LBehave
from Library.config import Config
import pytest



class TestJewelryPage:
    read_behave = LBehave()
    read_data = read_behave.read_data(Config.read_data)

    @pytest.mark.parametrize('length_',read_data)
    def test_jewelry(self,length_,_driver):
        lp=Jewelry(_driver)
        lp.Jewelry_module()
        lp.sort_by()
        lp.display()
        lp.View_As()
        lp.Filter_By_Price()
        lp.ATC_dis()
        # lp.AddToCart
        lp.Create_Your_Own_Jewelry()
        lp.J_Material()
        lp.length(length_)
        lp.pendant_radio()