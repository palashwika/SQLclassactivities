DROP TABLE IF EXISTS MissionCrew;
DROP TABLE IF EXISTS Crew;
DROP TABLE IF EXISTS Missions;
DROP TABLE IF EXISTS Spacecraft;
DROP TABLE IF EXISTS Planets;

CREATE TABLE Planets (
    planet_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    planet_type TEXT NOT NULL,
    distance_million_km REAL,
    has_rings INTEGER,
    discovered_year INTEGER
);

CREATE TABLE Spacecraft (
    spacecraft_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    launch_year INTEGER,
    status TEXT NOT NULL,
    planet_id INTEGER,
    FOREIGN KEY (planet_id) REFERENCES Planets(planet_id)
);

CREATE TABLE Missions (
    mission_id INTEGER PRIMARY KEY,
    mission_name TEXT NOT NULL,
    spacecraft_id INTEGER,
    target_planet_id INTEGER,
    launch_date TEXT,
    mission_status TEXT,
    budget_million REAL,
    FOREIGN KEY (spacecraft_id) REFERENCES Spacecraft(spacecraft_id),
    FOREIGN KEY (target_planet_id) REFERENCES Planets(planet_id)
);

CREATE TABLE Crew (
    crew_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    role TEXT NOT NULL,
    experience_years INTEGER,
    home_country TEXT
);

CREATE TABLE MissionCrew (
    mission_id INTEGER,
    crew_id INTEGER,
    hours_worked INTEGER,
    PRIMARY KEY (mission_id, crew_id),
    FOREIGN KEY (mission_id) REFERENCES Missions(mission_id),
    FOREIGN KEY (crew_id) REFERENCES Crew(crew_id)
);

INSERT INTO Planets VALUES
(1, 'Mars', 'Terrestrial', 225.0, 0, 1610),
(2, 'Jupiter', 'Gas Giant', 778.5, 1, 1610),
(3, 'Saturn', 'Gas Giant', 1434.0, 1, 1610),
(4, 'Europa', 'Moon', 628.3, 0, 1610),
(5, 'Titan', 'Moon', 1427.0, 1, 1655),
(6, 'Venus', 'Terrestrial', 108.2, 0, 1610),
(7, 'Neptune', 'Ice Giant', 4495.1, 1, 1846),
(8, 'Kepler-186f', 'Exoplanet', 4920000000.0, 0, 2014);

INSERT INTO Spacecraft VALUES
(101, 'Ares Explorer', 'Rover', 2028, 'Active', 1),
(102, 'Odyssey', 'Orbiter', 2026, 'Active', 2),
(103, 'Titan Voyager', 'Probe', 2030, 'Planned', 5),
(104, 'Europa Clipper', 'Orbiter', 2024, 'Active', 4),
(105, 'Solaris', 'Space Telescope', 2027, 'Active', NULL),
(106, 'Deep Horizon', 'Probe', 2025, 'Retired', 7),
(107, 'Venus Runner', 'Atmospheric Probe', 2029, 'Active', 6),
(108, 'Starlight', 'Space Telescope', 2031, 'Planned', 8);

INSERT INTO Missions VALUES
(201, 'Red Dawn', 101, 1, '2028-07-14', 'Completed', 850.0),
(202, 'Jupiter Storm', 102, 2, '2027-03-21', 'Active', 1200.0),
(203, 'Titan Seas', 103, 5, '2030-09-12', 'Planned', 2100.0),
(204, 'Europa Ice', 104, 4, '2026-11-05', 'Active', 1750.0),
(205, 'Deep Space Survey', 105, 8, '2027-01-30', 'Active', 950.0),
(206, 'Neptune Signal', 106, 7, '2025-06-18', 'Completed', 670.0),
(207, 'Venus Inferno', 107, 6, '2029-04-11', 'Planned', 430.0),
(208, 'Second Red Dawn', 101, 1, '2030-02-19', 'Planned', 920.0);

INSERT INTO Crew VALUES
-- USA
(301, 'Maya Chen', 'Mission Commander', 12, 'USA'),
(304, 'Noah Williams', 'Engineer', 5, 'USA'),
(311, 'Ethan Brooks', 'Pilot', 8, 'USA'),
(312, 'Grace Miller', 'Astrobiologist', 6, 'USA'),
(313, 'James Carter', 'Systems Engineer', 10, 'USA'),

(307, 'Amara Okafor', 'Data Scientist', 6, 'Nigeria'),
(308, 'Daniel Kim', 'Systems Engineer', 4, 'South Korea'),
(309, 'Elena Petrova', 'Planetary Scientist', 14, 'Russia'),
(310, 'Lucas Brown', 'Communications Officer', 3, 'Canada'),

-- Mexico
(302, 'Leo Martinez', 'Pilot', 7, 'Mexico'),
(314, 'Camila Torres', 'Geologist', 5, 'Mexico'),
(315, 'Diego Ramirez', 'Engineer', 9, 'Mexico'),
(316, 'Valeria Cruz', 'Data Scientist', 4, 'Mexico'),
(317, 'Mateo Hernandez', 'Robotics Specialist', 7, 'Mexico'),

-- India
(303, 'Aisha Patel', 'Astrobiologist', 9, 'India'),
(318, 'Arjun Mehta', 'Engineer', 6, 'India'),
(319, 'Priya Shah', 'Planetary Scientist', 11, 'India'),
(320, 'Rohan Kapoor', 'Pilot', 5, 'India'),
(321, 'Ananya Rao', 'Data Scientist', 8, 'India'),

-- Italy
(305, 'Sofia Rossi', 'Geologist', 11, 'Italy'),
(322, 'Marco Bianchi', 'Engineer', 7, 'Italy'),
(323, 'Giulia Romano', 'Astrobiologist', 6, 'Italy'),
(324, 'Luca Ferrari', 'Pilot', 9, 'Italy'),
(325, 'Chiara Conti', 'Mission Commander', 13, 'Italy'),

-- Japan
(306, 'Kenji Tanaka', 'Robotics Specialist', 8, 'Japan'),
(326, 'Yuki Sato', 'Engineer', 6, 'Japan'),
(327, 'Hiroshi Nakamura', 'Pilot', 10, 'Japan'),
(328, 'Aiko Watanabe', 'Data Scientist', 5, 'Japan'),
(329, 'Ren Ito', 'Systems Engineer', 7, 'Japan');

INSERT INTO MissionCrew VALUES
(201, 301, 420),
(201, 303, 380),
(201, 305, 350),
(201, 306, 410),

(202, 302, 510),
(202, 304, 470),
(202, 307, 430),

(203, 301, 290),
(203, 303, 310),
(203, 306, 275),

(204, 303, 520),
(204, 305, 480),
(204, 308, 450),

(205, 307, 390),
(205, 308, 420),
(205, 310, 350),

(206, 309, 610),
(206, 304, 550),

(207, 302, 270),
(207, 305, 300),

(208, 301, 180),
(208, 306, 210);


--SELECT name, experience_years, home_country FROM Crew GROUP BY home_country ORDER BY experience_years DESC;
--SELECT name, experience_years, home_country FROM Crew GROUP BY home_country;
--SELECT * FROM CREW ORDER BY home_country;
WITH RankedRows AS (
    SELECT 
        name,
        experience_years,
        home_country,
        ROW_NUMBER() OVER (
            PARTITION BY home_country 
            ORDER BY experience_years DESC
        ) AS rn
    FROM Crew
)
SELECT name, home_country, experience_years FROM RankedRows WHERE rn=1;