Summary:	Very powerful Quake style Konsole
Name:		yakuake
Version:	2.9.9
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/KDE
Source0:	http://download.kde.org/stable/yakuake/%{version}/src/%{name}-%{version}.tar.xz
Url:		http://www.kde-apps.org/content/show.php?content=29153
BuildRequires:	kdelibs4-devel
Requires:	konsole
Obsoletes:	kde4-%name <= 2.9.2
Provides:	kde4-%name = %version

%description
Yakuake is a Quake-style terminal emulator based on KDE Konsole technology.

%files -f %{name}.lang
%doc AUTHORS ChangeLog README TODO NEWS KDE4FAQ
%{_kde_bindir}/*
%{_kde_datadir}/applications/kde4/*.desktop
%{_kde_appsdir}/%{name}
%{_kde_appsdir}/kconf_update/%{name}*
%{_kde_configdir}/yakuake.knsrc
%{_kde_iconsdir}/hicolor/*/apps/*

#--------------------------------------------------------------------

%prep 
%setup -qn %{name}-%{version}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %name
