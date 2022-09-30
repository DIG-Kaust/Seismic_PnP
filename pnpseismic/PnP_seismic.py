import numpy as np
import pyproximal
from pyproximal.ProxOperator import _check_tau
from pyproximal import ProxOperator
from pyproximal.proximal import L2
from pyproximal.proximal import *
from pyproximal.optimization.primal import *
from pyproximal.optimization.primaldual import *
from pylops.optimization.leastsquares import RegularizedInversion


def PrimalDual_(proxf, proxg, A, x0, tau, mu, z=None, theta=1., niter=10,
               gfirst=True, callback=None, show=False):
    
    if show:
        tstart = time.time()
        print('Primal-dual: min_x f(Ax) + x^T z + g(x)\n'
              '---------------------------------------------------------\n'
              'Proximal operator (f): %s\n'
              'Proximal operator (g): %s\n'
              'Linear operator (A): %s\n'
              'Additional vector (z): %s\n'
              'tau = %10e\tmu = %10e\ntheta = %.2f\t\tniter = %d\n' %
              (type(proxf), type(proxg), type(A),
               None if z is None else 'vector', tau, mu, theta, niter))
        head = '   Itn       x[0]          f           g          z^x       J = f + g + z^x'
        print(head)

    x = x0.copy()
    xhat = x.copy()
    y = np.zeros(A.shape[0], dtype=x.dtype)
    yold = y.copy()
#     y = np.zeros(x0.shape, dtype=x.dtype)
    
    for iiter in range(niter):
        xold = x.copy()
        if gfirst:

            y = proxg.proxdual(yold + mu * A.matvec(xhat), mu)

            y_d = (y - yold - mu * A.matvec(xhat)) / mu *-1

            ATy = A.rmatvec(y)
            if z is not None:
                ATy += z
            x = proxf.prox(x - tau * ATy, tau)
            x_d = x + yold/mu
            xhat = x + theta * (x - xold)
            yold = y.copy()
        else:
            ATy = A.rmatvec(y)
            if z is not None:
                ATy += z
            x = proxf.prox(x - tau * ATy, tau)
            xhat = x + theta * (x - xold)
            y = proxg.proxdual(y + mu * A.matvec(xhat), mu)

        # run callback
        if callback is not None:
            callback(xhat, y_d)

        if show:
            if iiter < 10 or niter - iiter < 10 or iiter % (niter // 10) == 0:
                pf, pg = proxf(x), proxg(A.matvec(x))
                pf = 0. if type(pf) == bool else pf
                pg = 0. if type(pg) == bool else pg
                zx = 0. if z is None else np.dot(z, x)
                msg = '%6g  %12.5e  %10.3e  %10.3e  %10.3e      %10.3e' % \
                      (iiter + 1, x[0], pf, pg, zx, pf + pg + zx)
                print(msg)
    if show:
        print('\nTotal time (s) = %.2f' % (time.time() - tstart))
        print('---------------------------------------------------------\n')
    return x


# Plug and Play functions with different algorithms

class _Denoise(ProxOperator):
    r"""Denoiser of choice

    Parameters
    ----------
    denoiser : :obj:`func`
        Denoiser (must be a function with two inputs, the first is the signal
        to be denoised, the second is the `tau` constant of the y-update in
        the ADMM optimization
    dims : :obj:`tuple`
        Dimensions used to reshape the vector ``x`` in the ``prox`` method
        prior to calling the ``denoiser``

    """
    def __init__(self, denoiser, dims):
        super().__init__(None, False)
        self.denoiser = denoiser
        self.dims = dims

    def __call__(self, x):
        return 0.

    @_check_tau
    def prox(self, x, tau):
        x = x.reshape(self.dims)
        xden = self.denoiser(x, tau)
        return xden.ravel()
    
    
def PlugAndPlay_PrimalDual(proxf, denoiser, A, dims, x0, tau, mu, niter=10,
                gfirst=True, callback=None, show=False):
    
    # Denoiser
    proxpnp = _Denoise(denoiser, dims=dims)

    return PrimalDual_(proxf, proxpnp, A,  x0=x0, tau=tau, mu=mu,
                niter=niter, callback=callback, gfirst=gfirst,
                show=show)
