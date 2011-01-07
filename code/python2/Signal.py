# importing cmath makes exp and other math functions handle
# complex numbers
from cmath import *

class Signal(list):
    pass

class TimeSignal(Signal):
    """a signal represented as a sequence of values in time.
    """
    def fft(self):
        return FrequencySignal(fft(self))

        
class FrequencySignal(Signal):
    """a signal represented as a sequence of Complex numbers
    that encode amplitude and phase as a function of frequency.
    """
    def ifft(self):
        return TimeSignal(ifft(self))

def fft(h):
    """compute the discrete Fourier transform of the sequence h.
    Assumes that len(h) is a power of two.
    """
    N = len(h)

    # the Fourier transform of a single value is itself
    if N == 1: return h

    # recursively compute the FFT of the even and odd values
    He = fft(h[0:N:2])
    Ho = fft(h[1:N:2])

    # merge the half-FFTs
    j = complex(0,1)
    W = exp(2*pi*j/N)
    ws = [pow(W,k) for k in range(N)]
    H = [e + w*o for w, e, o in zip(ws, He+He, Ho+Ho)]
    return H


# make a signal with two sine components, f=6 and f=12
N=128
t = [1.0*i/N for i in range(N)]
h = [sin(2*pi*6*tk) + sin(2*pi*12*tk) for tk in t]

# compute the Fourier transform
H = fft(h)

# print the spectral density function
#sdf = [Hk * Hk.conjugate() for Hk in H]
#for i in range(N/2 + 1):
#    print '%d  %.3f' % (i, sdf[i].real)

#h = fft(H)
for i, tk in enumerate(h):
    print i, tk.real
