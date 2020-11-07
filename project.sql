--
-- PostgreSQL database dump
--

-- Dumped from database version 10.14 (Ubuntu 10.14-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.14 (Ubuntu 10.14-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: daily_reports; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.daily_reports (
    daily_report_id integer NOT NULL,
    daily_report_name character varying NOT NULL,
    project_id integer,
    employee_id integer,
    created_at timestamp without time zone DEFAULT now()
);


ALTER TABLE public.daily_reports OWNER TO vagrant;

--
-- Name: daily_reports_daily_report_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.daily_reports_daily_report_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.daily_reports_daily_report_id_seq OWNER TO vagrant;

--
-- Name: daily_reports_daily_report_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.daily_reports_daily_report_id_seq OWNED BY public.daily_reports.daily_report_id;


--
-- Name: employees; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.employees (
    employee_id integer NOT NULL,
    full_name character varying(100) NOT NULL,
    email character varying(50) NOT NULL,
    user_id character varying(20) NOT NULL,
    password character varying(20) NOT NULL,
    roles character varying
);


ALTER TABLE public.employees OWNER TO vagrant;

--
-- Name: employees_employee_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.employees_employee_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.employees_employee_id_seq OWNER TO vagrant;

--
-- Name: employees_employee_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.employees_employee_id_seq OWNED BY public.employees.employee_id;


--
-- Name: projects; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.projects (
    project_id integer NOT NULL,
    project_name character varying(50) NOT NULL,
    planned_start_date date NOT NULL,
    actual_start_date date,
    actual_end_date date,
    project_description character varying,
    project_location character varying,
    daily_reports integer
);


ALTER TABLE public.projects OWNER TO vagrant;

--
-- Name: projects_employees; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.projects_employees (
    employee_id integer,
    projects_id integer
);


ALTER TABLE public.projects_employees OWNER TO vagrant;

--
-- Name: projects_project_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.projects_project_id_seq
    AS integer
    START WITH 4000
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.projects_project_id_seq OWNER TO vagrant;

--
-- Name: projects_project_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.projects_project_id_seq OWNED BY public.projects.project_id;


--
-- Name: daily_reports daily_report_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.daily_reports ALTER COLUMN daily_report_id SET DEFAULT nextval('public.daily_reports_daily_report_id_seq'::regclass);


--
-- Name: employees employee_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.employees ALTER COLUMN employee_id SET DEFAULT nextval('public.employees_employee_id_seq'::regclass);


--
-- Name: projects project_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.projects ALTER COLUMN project_id SET DEFAULT nextval('public.projects_project_id_seq'::regclass);


--
-- Data for Name: daily_reports; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.daily_reports (daily_report_id, daily_report_name, project_id, employee_id, created_at) FROM stdin;
\.


--
-- Data for Name: employees; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.employees (employee_id, full_name, email, user_id, password, roles) FROM stdin;
1	Penny Pollack	penny.pollack@kpconst.com	poll0109	password	site supervisor
\.


--
-- Data for Name: projects; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.projects (project_id, project_name, planned_start_date, actual_start_date, actual_end_date, project_description, project_location, daily_reports) FROM stdin;
4000	New Hope Pool	2020-10-01	2020-11-01	\N	\N	\N	\N
\.


--
-- Data for Name: projects_employees; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.projects_employees (employee_id, projects_id) FROM stdin;
\.


--
-- Name: daily_reports_daily_report_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.daily_reports_daily_report_id_seq', 1, false);


--
-- Name: employees_employee_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.employees_employee_id_seq', 1, true);


--
-- Name: projects_project_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.projects_project_id_seq', 1, false);


--
-- Name: projects constraint_name; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.projects
    ADD CONSTRAINT constraint_name UNIQUE (daily_reports);


--
-- Name: daily_reports daily_reports_daily_report_name_key; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.daily_reports
    ADD CONSTRAINT daily_reports_daily_report_name_key UNIQUE (daily_report_name);


--
-- Name: daily_reports daily_reports_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.daily_reports
    ADD CONSTRAINT daily_reports_pkey PRIMARY KEY (daily_report_id);


--
-- Name: employees employees_full_name_key; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.employees
    ADD CONSTRAINT employees_full_name_key UNIQUE (full_name);


--
-- Name: employees employees_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.employees
    ADD CONSTRAINT employees_pkey PRIMARY KEY (employee_id);


--
-- Name: employees employees_user_id_key; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.employees
    ADD CONSTRAINT employees_user_id_key UNIQUE (user_id);


--
-- Name: projects projects_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.projects
    ADD CONSTRAINT projects_pkey PRIMARY KEY (project_id);


--
-- Name: projects projects_project_name_key; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.projects
    ADD CONSTRAINT projects_project_name_key UNIQUE (project_name);


--
-- Name: daily_reports daily_reports_daily_report_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.daily_reports
    ADD CONSTRAINT daily_reports_daily_report_id_fkey FOREIGN KEY (daily_report_id) REFERENCES public.projects(daily_reports);


--
-- Name: daily_reports daily_reports_employee_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.daily_reports
    ADD CONSTRAINT daily_reports_employee_id_fkey FOREIGN KEY (employee_id) REFERENCES public.employees(employee_id);


--
-- Name: projects_employees projects_employees_employee_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.projects_employees
    ADD CONSTRAINT projects_employees_employee_id_fkey FOREIGN KEY (employee_id) REFERENCES public.employees(employee_id);


--
-- Name: projects_employees projects_employees_projects_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.projects_employees
    ADD CONSTRAINT projects_employees_projects_id_fkey FOREIGN KEY (projects_id) REFERENCES public.projects(project_id);


--
-- Name: projects_employees projects_employees_projects_id_fkey1; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.projects_employees
    ADD CONSTRAINT projects_employees_projects_id_fkey1 FOREIGN KEY (projects_id) REFERENCES public.projects(project_id);


--
-- PostgreSQL database dump complete
--

