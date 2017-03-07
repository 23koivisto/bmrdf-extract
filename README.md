This program is designed to ingest the output xml from the British Museum SPARQL endpoint and return separate RDF metadata records for each object returned in this output. It is currently pretty stupid and does not have usability features.

The command takes a single argument: the xml file you wish for the program to read. Commands should read "sh bm.sh *something.xml*".

The output will generate in the same directory where the program is stored. A directory titled "bmrdf" will generate and the discrete metadata records will be generated with a BM ID number generated with a ".xml" file extension.

N.B.: The command currently looks at ONLY numeric BM URIs. Based on conversations with those in charge of the BM SPARQL endpoint, queries return redundant identifiers for each object. Assuming that each object will have one URI that is purely numeric, this program will return a total of XML records that is 1/3 the total returned URIs in the SPARQL output.