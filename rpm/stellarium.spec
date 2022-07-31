# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       stellarium

# >> macros
# << macros

Summary:    Planetary application
Version:    1.29.6
Release:    1
Group:      Qt/Qt
License:    GPLv2
URL:        https://github.com/fuchsmich/Stellarium-mobile
Source0:    %{name}-%{version}.tar.bz2
Source1:    stellarium-rpmlintrc
Source100:  stellarium.yaml
Requires:   sailfishsilica-qt5 >= 0.10.9
Requires:   qt5-qtdeclarative-import-localstorageplugin
Requires:   qt5-qtdeclarative-import-particles2
Requires:   qt5-qtpositioning
Requires:   qt5-qtsensors
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Positioning)
BuildRequires:  pkgconfig(Qt5Sensors)
BuildRequires:  desktop-file-utils

%description
Stellarium for Sailfish adapted from Stellarium Mobile source.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake5 

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
# >> files
# << files
