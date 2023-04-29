/**
 * Given a list of known currency conversion rates:
 * AUD -> USD: 0.7
 * USD -> JPY: 100
 * GBP -> USD: 1.3
 * 
 * Input are a list of conversion queries which include source currency and destination currency, return the corresponding rates.
 * For example,  queries can be:
 * 
 * USD -> GBP
 * AUD -> JPY
 * AUD -> GBP
 * 
 * If the rate cannot be deduced from the given rates, just return N/A
 * 
 */
import java.util.*;

public class CurrencyConversionQuery {

    public static void main(String[] args) {

        ConversionGraph graph = new ConversionGraph();

        Map<String, List<Conversion>> conversionMap = new HashMap<>();

        Conversion conversion1 =  new Conversion();
        conversion1.setSource("AUD").setDestination("USD").setRate(0.7);
        Conversion conversion2 = new Conversion();
        conversion2.setSource("USD").setDestination("AUD").setRate(1/0.7);

        Conversion conversion3 =  new Conversion();
        conversion3.setSource("USD").setDestination("JPY").setRate(100.0);
        Conversion conversion4 = new Conversion();
        conversion4.setSource("JPY").setDestination("USD").setRate(1/100.0);

        Conversion conversion5 =  new Conversion();
        conversion5.setSource("GBP").setDestination("USD").setRate(1.3);
        Conversion conversion6 = new Conversion();
        conversion6.setSource("USD").setDestination("GBP").setRate(1/1.3);

        conversionMap.put("AUD", Arrays.asList(conversion1));
        conversionMap.put("USD", Arrays.asList(conversion2, conversion3, conversion6));
        conversionMap.put("JPY", Arrays.asList(conversion4));
        conversionMap.put("GBP", Arrays.asList(conversion5));

        graph.setConversionMap(conversionMap);

        int n = 5;
        String[] sources =  {"USD", "AUD", "GBP", "SGD", "AUD"};
        String[] destinations = {"AUD", "GBP", "JPY", "USD", "AUD"};

        Double[] result = getConversionQueryRates(graph, sources, destinations, n);

        for (Double d : result) {
            System.out.println("Rate is: " + (d == null? "N/A": d));
        }

    }


    public static Double[] getConversionQueryRates(ConversionGraph graph, String[] sources, String[] destinations, int n) {

        Double[] rates =  new Double[n];

        for (int i = 0; i < n; i++) {
            String source = sources[i];
            String destination = destinations[i];

            rates[i] = getConversionRate(graph, source, destination);
        }

        return rates;

    }

    public static Double getConversionRate(ConversionGraph graph, String source, String destination) {

        if (source.equals(destination)) {
            return 1.0;
        }

        Queue<String> currencyQueue = new LinkedList<>();
        Map<String, Double> rateMap = new HashMap<>();
        Map<String, Boolean> visited =  new HashMap<>();

        Map<String, List<Conversion>> conversionMap = graph.getConversionMap();

        currencyQueue.add(source);
        rateMap.put(source, 1.0);

        while (!currencyQueue.isEmpty()) {
            String currentCurrency = currencyQueue.remove();
            visited.put(currentCurrency, Boolean.TRUE);
            Double currentRate = rateMap.getOrDefault(currentCurrency, 1.0);

            if (currentCurrency.equals(destination)) {
                return currentRate;
            }

            List<Conversion> conversions = conversionMap.getOrDefault(currentCurrency, Collections.emptyList());

            for (Conversion c: conversions) {
                String d = c.getDestination();
                Double r = c.getRate();
                
                if (!visited.getOrDefault(d, Boolean.FALSE)) {
                    currencyQueue.add(d);
                    rateMap.put(d, currentRate*r);
                }
            }
        }

        return null;
    }


    public static class Conversion {
        String source;
        String destination;
        Double rate;

        public String getDestination() {
            return this.destination;
        }

        public String getSource() {
            return this.source;
        }

        public Double getRate() {
            return this.rate;
        }

        public Conversion setDestination(String destination) {
            this.destination = destination;
            return this;
        }

        public Conversion setSource(String source) {
            this.source = source;
            return this;
        }

        public Conversion setRate(Double rate) {
            this.rate = rate;
            return this;
        }
    }

    public static class ConversionGraph  {

        Map<String, List<Conversion>> conversionMap;


        public Map<String, List<Conversion>> getConversionMap() {
            return this.conversionMap;
        }

        public void setConversionMap(Map<String, List<Conversion>> conversionMap) {
            this.conversionMap = conversionMap;
        }

    }

 }