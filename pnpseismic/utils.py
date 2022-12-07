import numpy as np

def callback0(x, xtrue, xhist, errhist):
    xhist.append(x)
    errhist.append(np.linalg.norm(x - xtrue)/np.linalg.norm(xtrue))
    
def callback(x, y, xtrue, xhist, yhist, errhistx, errhisty):
    xhist.append(x)
    yhist.append(y)
    errhistx.append(np.linalg.norm(x - xtrue) / np.linalg.norm(xtrue))
    errhisty.append(np.linalg.norm(y - xtrue) / np.linalg.norm(xtrue))
       
def snr(xref, xest):
    xrefv = np.mean(np.abs(xref) ** 2)
    return 10. * np.log10( xrefv / np.mean(np.abs(xref - xest)**2))