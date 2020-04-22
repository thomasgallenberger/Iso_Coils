# Iso_Coils
Plot the coils for an isodynamic stellarator
The Plot_helical_coils.py file will plot the coils and can also create the .sldcrv files if you prefer. It can also plot the results of Aaronbader's flf code on the graph with the coils. 

To get the .sldcrv files into solidworks use either download them or generate them with the Plot_helical_coils.py code, then:
   insert -> curves -> curve through xyz points
   A menu will pop up, click browse and select the file you want 
If you try to plot these coils with python or another language, it is important to note that the files are xzy because the y axis is the vertical axis in solidworks. 
