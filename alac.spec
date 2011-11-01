%define name            alac
%define libname         %mklibname %name
%define develname       %mklibname -d %name
%define stdevelname     %mklibname -d -s %name

Name:           %name
Version:        0.1
Release:        %mkrel 1.20111026
Group:          Sound
Summary:        Apple Lossless Audio Codec (ALAC)
License:        Apache License
URL:            http://alac.macosforge.org/
Source0:        %{name}-%{version}.tar.xz
Patch0:         alac-0.1-makefile.patch

%description
The Apple Lossless Audio Codec (ALAC) is an audio codec developed by Apple and
supported on iPhone, iPad, most iPods, Mac and iTunes.  ALAC is a data
compression method which reduces the size of audio files with no loss
of information.  A decoded ALAC stream is bit-for-bit identical to the original
uncompressed audio file.

%package -n %libname
Summary:        Apple Lossless Audio Codec
Group:          System/Libraries
License:        Apple Public Source License

%description -n %libname
The Apple Lossless Audio Codec (ALAC) is an audio codec developed by Apple and
supported on iPhone, iPad, most iPods, Mac and iTunes.  ALAC is a data
compression method which reduces the size of audio files with no loss
of information.  A decoded ALAC stream is bit-for-bit identical to the original
uncompressed audio file.

%package -n %develname
Summary:        Apple Lossless Audio Codec
Group:          Development/C++
Requires:       %libname = %{version}
License:        Apple Public Source License

%description -n %develname
The Apple Lossless Audio Codec (ALAC) is an audio codec developed by Apple and
supported on iPhone, iPad, most iPods, Mac and iTunes.  ALAC is a data
compression method which reduces the size of audio files with no loss
of information.  A decoded ALAC stream is bit-for-bit identical to the original
uncompressed audio file.

%package -n %stdevelname
Summary:        Apple Lossless Audio Codec
Group:          Development/C++
Requires:       %develname
License:        Apple Public Source License

%description -n %stdevelname
The Apple Lossless Audio Codec (ALAC) is an audio codec developed by Apple and
supported on iPhone, iPad, most iPods, Mac and iTunes.  ALAC is a data
compression method which reduces the size of audio files with no loss
of information.  A decoded ALAC stream is bit-for-bit identical to the original
uncompressed audio file.

%package -n alacconvert
Summary:        Apple Lossless Audio Codec
Group:          Sound

%description -n alacconvert
The Apple Lossless Audio Codec (ALAC) is an audio codec developed by Apple and
supported on iPhone, iPad, most iPods, Mac and iTunes.  ALAC is a data
compression method which reduces the size of audio files with no loss of
information.  A decoded ALAC stream is bit-for-bit identical to the original
uncompressed audio file.

This package contains a command-line utility to convert the ALAC format.

%prep
%setup -q
%patch0

%build
for d in codec convert-utility; do
    %__make -C "$d" \
        OPTFLAGS="%{optflags}" \
        CC="%__cxx"
done

%install
%__install -D -m0755 convert-utility/alacconvert "%{buildroot}%{_bindir}/alacconvert"

%__install -d "%{buildroot}%{_includedir}"
%__cp -a codec/*.h "%{buildroot}%{_includedir}/"

%__install -D -m0644 codec/libalac.a "%{buildroot}%{_libdir}/libalac.a"
%__cp -a codec/libalac.so* "%{buildroot}%{_libdir}/"

%clean
%{?buildroot:%__rm -rf "%{buildroot}"}

%files -n %libname
%defattr(-,root,root)
%doc codec/APPLE_LICENSE.txt
%{_libdir}/libalac.so.0
%{_libdir}/libalac.so.0.1

%files -n %develname
%defattr(-,root,root)
%{_includedir}/*.h
%{_libdir}/libalac.so

%files -n %stdevelname
%defattr(-,root,root)
%{_libdir}/libalac.a

%files -n alacconvert
%defattr(-,root,root)
%{_bindir}/alacconvert
%doc ReadMe.txt ALACMagicCookieDescription.txt LICENSE
