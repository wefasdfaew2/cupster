﻿/*
 * Created by SharpDevelop.
 * User: Lars Magnus
 * Date: 12.06.2014
 * Time: 20:52
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using Nancy.Hosting.Self;

namespace webstats
{
	class Program
	{
		public static void Main(string[] args)
		{
			HostConfiguration hc = new HostConfiguration();
			hc.UrlReservations.CreateAutomatically = true;
			using (var host = new NancyHost(hc, new Uri("http://localhost:4444")))
			{
			   host.Start();
			   Console.ReadLine();
			}
		}
	}
}