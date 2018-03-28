# ns-sni
Code for adding certs to the SNI cs vserver

Need to have the NITRO API python egg, can be downloaded and installed via Download page on the NS.

User making calls needs following cmd policy:
(add system file (.*)(key|cert))|(add ssl certKey sni_.*)|(bind ssl vserver cs_sni.o.e.*certkeyName\ssni_.*)
