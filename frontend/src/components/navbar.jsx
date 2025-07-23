import { Link } from "react-router-dom"
import React from "react"
import { motion } from "framer-motion"
import { TwitterIcon, GithubIcon, LinkedInIcon } from "./icons"

const NavBar = () => {
	return (
		<header className="w-full px-8 font-medium flex items-center justify-between dark:text-light fixed z-10 bg-white shadow-md">
			<div className="w-full flex justify-between items-center">
				<Link to="register">
					<img
						src="../../public/images/logo.png"
						alt=""
						className="h-20 w-auto"
					/>
				</Link>
				<nav className="flex items-center justify-center">
					<Link to="/login" className="mx-4 ml-10">
						Login
					</Link>
					<Link to="/register" className="mx-4">
						Register
					</Link>
				</nav>

				<nav className="flex items-center justify-center flex-wrap">
					<motion.a
						href="https://www.linkedin.com/in/justin-cui-775819246/"
						target="_blank"
						className="w-6 mx-6"
						whileHover={{ y: -2 }}
						whileTap={{ scale: 0.9 }}
					>
						<LinkedInIcon />
					</motion.a>

					<motion.a
						href="https://github.com/JingQunCui"
						target="_blank"
						className="w-6 mr-6"
						whileHover={{ y: -2 }}
						whileTap={{ scale: 0.9 }}
					>
						<GithubIcon />
					</motion.a>

					<motion.a
						href="https://twitter.com/chatterfloo"
						target="_blank"
						className="w-6 mr-6"
						whileHover={{ y: -2 }}
						whileTap={{ scale: 0.9 }}
					>
						<TwitterIcon />
					</motion.a>
				</nav>
			</div>
		</header>
	)
}

export default NavBar
