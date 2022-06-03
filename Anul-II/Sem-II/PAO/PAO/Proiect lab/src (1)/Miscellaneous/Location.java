package Miscellaneous;

public class Location {

    private String street_name;
    private int building_number;
    private String country;
    private String county;
    private String city;

    public Location(String street_name, int building_number, String country, String county, String city) {
        this.street_name = street_name;
        this.building_number = building_number;
        this.country = country;
        this.county = county;
        this.city = city;
    }

    public String getStreet_name() {
        return street_name;
    }

    public void setStreet_name(String street_name) {
        this.street_name = street_name;
    }

    public int getBuilding_number() {
        return building_number;
    }

    public void setBuilding_number(int building_number) {
        this.building_number = building_number;
    }

    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public String getCounty() {
        return county;
    }

    public void setCounty(String county) {
        this.county = county;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
}
