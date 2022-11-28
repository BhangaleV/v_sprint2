Feature: Jewelry

  Scenario: click on Jewelry
    Given Open the browser and enter demo web shop url and click on jewelry category
    Then Click on sort by dropdown list options
    And Click on "Name: A to Z" then "Name: Z to A" then "Price: Low to High" then "Price: High to Low" then "Created On"
    Then Click on Display by
    And Click on 4 then 8 then 12
    Then Click on Filter By Price
    And Click on filter by 0.00-500.00 then 500.00-700.00 then 700.00-2000.00
    Then Click on View as
    And Click on Grid As View and then List As View
    Then Click on one of the product and check the description
    And come back and click on another product description and come back
    And click on another product description
    And come back and click on another product description
    And come back and click on another product
    Then click on Create Your Own Jewelry
    Then Click on Material dropdown list Options
    And Click on "Gold 0,5mm" then "Gold 1mm" then "Silver 1mm"
    Then Enter the length in Length in cm Field
    Then CLick on Pendant Radio Button Option
    And Click on "Ladybug" then "Heart" then "Star" then "None"
    And close the browser